import logging
from logging.handlers import RotatingFileHandler

def setup_logging(log_file):

    logging.basicConfig(level=logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    handler = RotatingFileHandler(log_file, maxBytes=10 * 1024 * 1024, backupCount=1)
    handler.setFormatter(formatter)

    root_logger = logging.getLogger()
    root_logger.addHandler(handler)
