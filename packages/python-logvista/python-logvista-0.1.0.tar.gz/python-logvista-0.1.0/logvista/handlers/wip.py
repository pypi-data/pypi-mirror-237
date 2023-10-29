import logging
import time
from logvista_handler import LogvistaHandler


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
lv = LogvistaHandler("dev_sample2")
lv.setLevel(logging.DEBUG)
logger.addHandler(lv)

try:
    raise Exception("test")
except Exception as e:
    logger.error(e)