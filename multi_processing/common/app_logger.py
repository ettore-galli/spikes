import logging


def make_logger(name: str, log_file: str):
    logger = logging.getLogger(__name__)

    logging.basicConfig(filename=log_file, encoding="utf-8", level=logging.DEBUG)

    return logger
