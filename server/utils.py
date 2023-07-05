"""Utilities Module."""


from logging import StreamHandler, DEBUG, getLogger, FileHandler
from sys import stdout


def get_logger_to_file(logger_name: str, file_name: str):
    """Returns a File logger instance."""
    logger = getLogger(logger_name)
    logger.setLevel(DEBUG)
    logger.addHandler(FileHandler(file_name))
    return logger


def get_logger_to_stdout(logger_name: str):
    """Returns a stdout logger instance."""
    logger = getLogger(logger_name)
    logger.setLevel(DEBUG)
    logger.addHandler(StreamHandler(stdout))
    return logger
