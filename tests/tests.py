from tests import test_utils
from utils import orc_engine
from utils.utils import init_log

log = init_log()

TEST_URL = 'http://i.imgur.com/31d5L5y.jpg'


def test_login_fail():
    try:
        orc_engine.space_file(filename='a.jpg', api_key="ggg")
    except ConnectionError as e:
        pass
    else:
        raise Exception("The api successfully log in with wrong credentials")
    try:
        orc_engine.space_url(url=TEST_URL, api_key="ggg")
    except ConnectionError as e:
        pass
    else:
        raise Exception("The api successfully log in with wrong credentials")
    

def test_login_success():
    test_utils.validate_file_result(orc_engine.space_file(filename='a.jpg'))
    test_utils.validate_url_result(orc_engine.space_url(url=TEST_URL))