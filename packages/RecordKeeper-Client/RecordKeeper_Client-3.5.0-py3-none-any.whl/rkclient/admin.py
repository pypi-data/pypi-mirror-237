import json
import logging
import time
from typing import Tuple, Optional
from importlib.metadata import version
from uuid import UUID

from rkclient.query import RKQuery
from rkclient.request import RequestHelper

log = logging.getLogger("rkclient")

RK_VERSION = version('RecordKeeper_Client')


class RKAdmin:
    """
    This class is not supposed to be used by normal RK user, but by RK administrator or in tests.
    """

    def __init__(self,
                 query_url: str,
                 graph_builder_url: str,
                 timeout_sec: int = 5,
                 insecure: bool = True,
                 user_auth: str = '',
                 puc_auth: str = ''):
        self.query_client = RKQuery(query_url, timeout_sec=timeout_sec, insecure=insecure,
                                    user_auth=user_auth, puc_auth=puc_auth)
        graph_builder_url = graph_builder_url.rstrip('/')
        log.info(f"Connecting to Graph Builder: {graph_builder_url}")
        self.graph_builder_client = RequestHelper(graph_builder_url, timeout_sec=timeout_sec, insecure=insecure,
                                                  user_auth=user_auth, puc_auth=puc_auth,
                                                  user_agent=f'recordkeeper-client-{RK_VERSION}')

    def check_connections(self) -> Tuple[str, bool]:
        msg, ok = self.graph_builder_client.get("/info")
        if not ok:
            return f"Graph Builder connection error: {msg}", False
        msg, ok = self.query_client.get_info()
        if not ok:
            return f"Receiver connection error: {msg}", False
        return 'OK', True

    def graph_rebuild(self) -> Tuple[str, bool]:
        """
        :return: first element: error message or 'OK'
                 second element: True for success, False for error
        """
        text, ok = self.graph_builder_client.post("/rebuild", "{}")
        if not ok:
            return f"Starting rebuilding process failed: {text}", False
        return 'OK', True

    def graph_flush(self) -> Tuple[str, bool]:
        """
        Waits till all PEMs from queue have been added to graph.
        :return: first element: error message or 'OK'
                 second element: True for success, False for error
        """
        start_time = time.time()
        text, ok = self.graph_builder_client.post("/flush", "{}")
        total_flush_time = time.time() - start_time
        if not ok:
            return f"flushing queue failed: {text}", False
        return f"flushing queue finished, in {total_flush_time:.2f}s", True

    def graph_verify(self, check_pems: bool = True, check_artifacts: bool = True) -> Tuple[str, bool]:
        """
        Starts sql vs graph comparison.
        :return: first element: json with "msg" field, containing error message or report (containing newlines).
                 second element: True for success, False for error
        """
        text, ok = self.graph_builder_client.post(
            "/verify",
            json.dumps({"check_pems": check_pems, "check_artifacts": check_artifacts})
        )
        if not ok:
            return f"Verifying integrity failed: {text}", False
        return text, True

    def artifacts_verify_connections(self) -> Tuple[Optional[UUID], str, bool]:
        """
        Starts a verification process which looks for Artifacts not connected to any PEM.
        The result of it will be saved in report pointed by the returned UUID.
        :return: first element: report_id in UUID format.
                 second element: error message
                 second element: True for success, False for error
        """
        result, ok = self.query_client.query_request.post("/verify_artifact_connections", "{}")
        if not ok:
            return None, f"Starting Artifact connection check failed: {result}", False
        result_json = json.loads(result)
        report_id = UUID(result_json['report_id'])
        return report_id, '', True

    def artifacts_remove_unconnected(self, report_id: UUID) -> Tuple[Optional[UUID], str, bool]:
        """
        Starts a removal process which. The result of it will be also saved in report.
        :return: first element: report_id in UUID format.
                 second element: error message
                 second element: True for success, False for error
        """
        result, ok = self.query_client.query_request.post(f"/remove_unconnected_artifacts/{report_id}", "{}")
        if not ok:
            return None, f"Starting Artifacts removal failed: {result}", False
        result_json = json.loads(result)
        report_id = UUID(result_json['report_id'])
        return report_id, '', True

    def get_report(self, report_id: str) -> Tuple[str, bool]:
        """
        Returns content of report.
        :return: first element: json with "report" and "status" field, or string error message.
                 second element: True for success, False for error
        """
        text, ok = self.query_client.query_request.get(f"/report/{report_id}")
        if not ok:
            return f"Getting report failed: {text}", False
        return text, True

    def get_graph_info(self) -> Tuple[str, bool]:
        """
        Returns json with fields as in GraphBuilderInfo class - the GB state. Use `deserialize_graph_builder_info` for easy parsing.
        :return: check class description
        """
        text, ok = self.graph_builder_client.get("/info")
        return text, ok

    def clean_dbs(self) -> Tuple[str, bool]:
        """
        Completely erases both sql and graph dbs - use only in tests. Needs admin permission from auth token.
        :return: first element: error message or 'OK'
                 second element: True for success, False for error
        """
        text, ok = self.query_client.query_request.post("/clean", "{}")
        if not ok:
            return f"Cleaning db failed: {text}", False
        return 'OK', True
