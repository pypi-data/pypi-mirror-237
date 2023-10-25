import logging
from handlers.logvista_handler import LogvistaHandler

logger = logging.getLogger("vista")
logger.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
logger.addHandler(stream_handler)

vista_handler = LogvistaHandler(
    system_name="vistatest", host="localhost:8000", url="/"
)
vista_handler.setLevel(logging.DEBUG)
logger.addHandler(vista_handler)

logger.info("info")
exit(0)