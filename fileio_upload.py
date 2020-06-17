"""
A command line utility to allow for quick file transfers.

Usage: python3 fileio_upload.py test.txt
This command will print the file.io link and will also copy the link to clipboard.
Optional arguments
    --noclip will not copy link to clipboard after upload
    -j will push the link the a phone connected through Join by Joaoapps.

Author: David Chen
"""
import requests
import json
import pyperclip
import argparse
import pathlib

# this should be of the basic form below:
# https://joinjoaomgcd.appspot.com/_ah/api/messaging/v1/sendPush?deviceId=???&apikey=???
JOIN_API_URL = 'https://joinjoaomgcd.appspot.com/_ah/api/messaging/v1/sendPush?deviceId=7a050437f66742919d68fb6b51b9c230&apikey=a174dac143094445a35aaf717c2dd875'
# JOIN_API_URL = ''


def get_url_from_resp(resp):
    """ Return file.io link from API response """
    return json.loads(resp.content)['link']


def upload_to_fileio(file_name):
    """ Upload file to file.io, return response """
    url = 'https://file.io/'
    cwd = pathlib.Path().absolute()

    files = {
        'file': open(cwd / file_name, 'rb')
    }

    resp = requests.post(url, files=files)
    return resp


def join_push_url(url):
    """ Push URL to to device with API key as specified in JOIN_API_URL """
    url = JOIN_API_URL + '&url=' + url
    requests.get(url)
    print('Pushed to Join')


def copy_url(url):
    """ Set clipboard to URL """
    pyperclip.copy(url)
    print('Set clipboard to: ' + url)


def parser():
    """ Parse command line arguments and return file path and additional flags  """
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='upload this file to file.io')
    parser.add_argument('--noclip', action='store_true', help='do not copy file.io url to clipboard')
    parser.add_argument('-j', '--join', action='store_true', help='push url and open on mobile')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parser()
    resp = upload_to_fileio(args.file)
    url = get_url_from_resp(resp)
    if args.noclip:
        print(url)
    else:
        copy_url(url)
    if args.join:
        join_push_url(url)