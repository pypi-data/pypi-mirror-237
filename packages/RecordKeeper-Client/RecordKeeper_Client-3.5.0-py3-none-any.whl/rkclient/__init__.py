from rkclient.client import RKClient, PEM, Artifact
from rkclient.serialization import ArtifactSerialization, PEMSerialization, ReceiverInfo, QueryInfo, GraphBuilderInfo, \
    deserialize_receiver_info, deserialize_query_info, deserialize_graph_builder_info
from rkclient.admin import RKAdmin
from rkclient.query import RKQuery
from rkclient.factory import RKClientFactory

import os
import logging

LOG_FORMAT = '[%(asctime)s] - %(levelname)s - RKClient: %(message)s'
LOG_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

log = logging.getLogger("rkclient")
log_handler = logging.StreamHandler()
log_handler.setFormatter(logging.Formatter(LOG_FORMAT, datefmt=LOG_DATE_FORMAT))
log.addHandler(log_handler)
log.setLevel(os.getenv("LOG_LEVEL", "INFO"))
# this is needed so that when client of this library uses root logger, RKClient won't propagate its logs to it,
# which would result in duplicate entries
log.propagate = False
