import json
import logging
import os

# from utils import consts
from utils.consts import LOG_DIR


def init_log():
    from datetime import datetime
    date_time = datetime.now().strftime("%d_%m_%H:%M:%S")
    log_folder = os.path.join(get_project_root_path(), LOG_DIR)
    if not os.path.exists(log_folder):
        os.mkdir(log_folder)
    file_name = os.path.join(log_folder, f'{date_time}.log')
    logging.basicConfig(filename=file_name, level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s',
                        datefmt='%d-%m-%YT%H:%M:%S')
    return logging


def get_project_root_path():
    return os.path.realpath('.').split("tests")[0]


def get_expected_data(table_name):
    expected_data_file_path = os.path.join(get_project_root_path(), 'data_source', table_name)
    with open(f"{expected_data_file_path}.json") as f:
        read_data = f.read()
    return json.loads(read_data)