from utils.utils import init_log

log = init_log()
FILE_TEXT ='PROGRAMMER INTERVIEW\r\nCan you work under ' \
           'pressure ?\r\nYes, of course\r\n3 months later\r\n'
LINK_TEXT = 'YEAN, IF you como GO AHEAD AND RUN OCR\r\nON ' \
            'THAT DOCUMENT SO THAT CTRL-F WORKS...\r\nTHAT ' \
            'WOULD BE\r\nGREAT...\r\nm enerator.net\r\n'
def validate_file_result(out):
    assert not out['IsErroredOnProcessing'], f'error on processing occurred.\n{out}'
    result = out['ParsedResults'][0]
    assert result['FileParseExitCode'] == 1, f'Parsing exit code error, Expected: 1.{out}'
    assert result['ParsedText'] == FILE_TEXT, f'plain text not as expected.\n{out}'
    assert result['TextOrientation'] == '0', f'Wrong text orientation.\n{out}'
    log.info(f'--1--> {type(out)}')
    log.info(f'--1--> {out}')
    
    
def validate_url_result(out):
    log.info(f'--2--> {type(out)}')
    log.info(f'--2--> {out}')
    assert not out['IsErroredOnProcessing'], f'error on processing occurred.\n{out}'
    result = out['ParsedResults'][0]
    assert result['FileParseExitCode'] == 1, f'Parsing exit code error, Expected: 1.{out}'
    assert result['ParsedText'] == LINK_TEXT, f'plain text not as expected.\n{out}'
    assert result['TextOrientation'] == '0', f'Wrong text orientation.\n{out}'