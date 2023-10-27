import logging.config
import os
import warnings

from bamt.config import config

log_file_path = config.get(
    "LOG", "log_conf_loc", fallback="log_conf_path is not defined"
)

if not os.path.isdir(os.path.join(os.path.expanduser("~"), "BAMT")):
    os.mkdir(os.path.join(os.path.expanduser("~"), "BAMT"))

try:
    logging.config.fileConfig(log_file_path)
except BaseException:
    log_file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "logging.conf"
    )
    logging.config.fileConfig(log_file_path)
    warnings.warn(
        "Reading log path location from config file failed. Default location will be used instead."
    )

logger_builder = logging.getLogger("builder")
logger_network = logging.getLogger("network")
logger_preprocessor = logging.getLogger("preprocessor")
logger_nodes = logging.getLogger("nodes")
logger_display = logging.getLogger("display")

logging.captureWarnings(True)
logger_warnings = logging.getLogger("py.warnings")
