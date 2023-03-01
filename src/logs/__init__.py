import json_log_formatter

import logging

formatter = json_log_formatter.JSONFormatter()
json_handler = logging.FileHandler(filename='./logs/UniversityListLogs.json')
json_handler.setFormatter(formatter)

logger = logging.getLogger('my_json')


def get_logger():
    if not logger.hasHandlers():
        logger.addHandler(json_handler)
        logger.setLevel(logging.INFO)
        return logger


log = get_logger()
