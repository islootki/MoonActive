
from tests import consts
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
    out = orc_engine.space_url(url=TEST_URL)
    assert not out['IsErroredOnProcessing'], f'error on processing occurred.\n{out}'
    result = out['ParsedResults'][0]
    assert result['FileParseExitCode'] == 1, f'Parsing exit code error, Expected: 1.{out}'
    assert result['ParsedText'] == consts.LINK_TEXT, f'plain text not as expected.\n{out}'
    assert result['TextOrientation'] == '0', f'Wrong text orientation.\n{out}'
    out2 = orc_engine.space_file(filename='a.jpg')
    assert not out2['IsErroredOnProcessing'], f'error on processing occurred.\n{out2}'
    result = out2['ParsedResults'][0]
    assert result['FileParseExitCode'] == 1, f'Parsing exit code error, Expected: 1.{out2}'
    assert result['ParsedText'] == consts.FILE_TEXT, f'plain text not as expected.\n{out2}'
    assert result['TextOrientation'] == '0', f'Wrong text orientation.\n{out2}'


def test_check_file_types():
    file_names = ['test_pic.bmp', 'test_pic.gif', 'test_pic.jpg', 'test_pic.pdf', 'test_pic.png', 'test_pic.tiff']
    for file_name in file_names:
        out = orc_engine.space_file(filename=file_name)
        assert not out['IsErroredOnProcessing'], f'error on processing occurred.\n{out}'
        result = out['ParsedResults'][0]
        assert result['FileParseExitCode'] == 1, f'Parsing exit code error, Expected: 1.{out}'
        assert result['ParsedText'] == consts.DIFF_TYPES_TEST_TEXT, f'plain text not as expected.\n{out}'
        assert result['TextOrientation'] == '0', f'Wrong text orientation.\n{out}'