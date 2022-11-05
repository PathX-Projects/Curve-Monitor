import logging

from .utils import get_logfile

formatter = logging.Formatter('%(module)s : %(levelname)s : %(asctime)s : %(message)s')

# Get logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Get logfile name & setup file handler
logfile = get_logfile()
file_handler = logging.FileHandler(logfile)
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.WARN)

# Setup stream handler
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

# Add handlers
logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def logged(_func):
    def wrapper(*args, **kwargs):
        try:
            return _func(*args, **kwargs)
        except Exception as e:
            logger.exception(f'Error occurred when running function {_func.__name__}', exc_info=e)
            raise e
    return wrapper