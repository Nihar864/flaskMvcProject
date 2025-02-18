import logging
from logging.handlers import RotatingFileHandler


def get_logger():
    logger = logging.getLogger("FlaskMvcProject")

    if logger.hasHandlers():
        logger.handlers.clear()
    logger.setLevel(logging.DEBUG)

    # request_id_context_var = contextvars.ContextVar('request_id', default=None)

    file_handler = RotatingFileHandler("app.log")
    file_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %("
        "message)s\n")
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    logger.propagate = False

    return logger
