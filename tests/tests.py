from utils import orc_engine
from utils.utils import init_log

log = init_log()


def test_login_fail():
    try:
        orc_engine.space_file(filename='a.jpg', api_key="ggg")
    except ConnectionError as e:
        pass
    else:
        raise Exception("The api successfully log in with wrong credentials")
    try:
        orc_engine.space_url(url='http://i.imgur.com/31d5L5y.jpg', api_key="ggg")
    except ConnectionError as e:
        pass
    else:
        raise Exception("The api successfully log in with wrong credentials")
    

