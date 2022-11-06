from os import getcwd, mkdir
from os.path import join, isdir
from typing import Union

def get_logfile() -> str:
    log_dir = join(getcwd(), 'logs')
    if not isdir(log_dir):
        mkdir(log_dir)
    return join(log_dir, 'log.txt')


def get_index(_iterable, func) -> Union[int, None]:
    """
    :param _iterable:
    :param func: Function should return a boolean (True or false)
    """
    for i, v in enumerate(_iterable):
        if func(v):
            return i
    return None