
import logging


def init_log():
    from datetime import datetime
    date_time = datetime.now().strftime("%d_%m_%H%M")
    LOG_FILENAME = f'{date_time}_.log'
    print(LOG_FILENAME)
    logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s',
                        datefmt='%d/%m/%YT%H:%M:%S')
    return logging