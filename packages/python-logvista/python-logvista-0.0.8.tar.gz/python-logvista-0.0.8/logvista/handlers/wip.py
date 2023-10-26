import logging
import time
from logvista_handler import LogvistaHandler


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
lv = LogvistaHandler("dev_sample")
lv.setLevel(logging.DEBUG)
logger.addHandler(lv)

try:
    raise Exception("test")
except Exception as e:
    logger.error("error")
    time.sleep(1)
    logger.error("included error", exc_info=True)

logger.info("info")
time.sleep(1)
logger.info("info2", exc_info=True)