import json
import os

from utils.utils import init_log

log = init_log()
import requests


IMAGES_DIR = 'images_dir'


def space_file(filename, overlay=False, api_key='6d14c0073188957', language='eng'):
    """
    The image should be placed in images_dir, only the name should be provided to the method
    :return: dict
    """
    log.debug(f"space_file filename={filename}, overlay={overlay}, api_key={api_key}, language={language}")
    filename = os.path.join(os.path.realpath('.').split("utils")[0], IMAGES_DIR, filename)
    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    return check_output(r)


def space_url(url, overlay=False, api_key='6d14c0073188957', language='eng'):
    log.debug(f"space_file url={url}, overlay={overlay}, api_key={api_key}, language={language}")
    payload = {'url': url,
               'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    r = requests.post('https://api.ocr.space/parse/image',
                      data=payload,
                      )
    return check_output(r)


def check_output(r):
    if r.status_code == 403:
        raise ConnectionError(f'{r.__dict__}')
    assert r.status_code == 200, f'{r.__dict__}'
    log.info(r.content.decode())
    return json.loads(r.content.decode())