import logging
from config import LOG_FILE

# Create a custom logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def setup_logger():
    # Create handlers
    c_handler = logging.StreamHandler()
    f_handler = logging.FileHandler(LOG_FILE)
    c_handler.setLevel(logging.WARNING)
    f_handler.setLevel(logging.INFO)

    # Create formatters and add it to handlers
    c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    c_handler.setFormatter(c_format)
    f_handler.setFormatter(f_format)

    # Add handlers to the logger
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)

    return logger

logger = setup_logger()

def log_info(message):
    logger.info(message)
    for handler in logger.handlers:
        handler.flush()

def log_warning(message):
    logger.warning(message)
    for handler in logger.handlers:
        handler.flush()

def log_error(message):
    logger.error(message)
    for handler in logger.handlers:
        handler.flush()
