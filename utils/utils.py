
import logging
import os

LOG_DIR = "log_dir"


def init_log():
    from datetime import datetime
    date_time = datetime.now().strftime("%d_%m_%H%M")
    file_name = os.path.join(os.path.realpath('.').split("tests")[0], LOG_DIR, f'{date_time}_.log')
    logging.basicConfig(filename=file_name, level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s',
                        datefmt='%d/%m/%YT%H:%M:%S')
    return logging