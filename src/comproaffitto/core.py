"""Main module."""
from comproaffitto import logs

logger = logs.get_logger(__name__)


def a_function() -> str:
    """Say hello to the world."""
    logger.debug("Generating hello world string")
    return "Hello World!"
