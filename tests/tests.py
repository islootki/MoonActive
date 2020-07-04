

from utils.utils import init_log

logging = init_log()


def test_1():
    logging.debug('This message should go to the log file')
    logging.debug('This message should go to the log file')
    logging.info('very_good!')
    assert 1 == 1

