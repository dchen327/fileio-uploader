"""
A command line utility to allow for easy file transfers.

Usage: python3 fileio_upload.py test.txt
This command will print the file.io link and will also copy the link to clipboard.
Optional flag -j will push the link the a phone connected through Join by Joaoapps.

Author: David Chen
"""
import requests
import json
import pyperclip
import argparse

# this should be of the basic form below:
# https://joinjoaomgcd.appspot.com/_ah/api/messaging/v1/sendPush?deviceId=???&apikey=???
JOIN_API_URL = 'https://joinjoaomgcd.appspot.com/_ah/api/messaging/v1/sendPush?deviceId=7a050437f66742919d68fb6b51b9c230&apikey=a174dac143094445a35aaf717c2dd875'


def get_link_from_resp(resp):
    """ Return file.io link from API response """
    return json.loads(resp.content)['link']


def upload_to_fileio(file_name):
    """ Upload file to file.io, return response """
    url = 'https://file.io/'

    files = {
        'file': open(file_name, 'rb')
    }

    resp = requests.post(url, files=files)
    return resp


def join_push_url(url):
    """ Push URL to to device with API key as specified in JOIN_API_URL """
    url = JOIN_API_URL + '&url=' + url
    requests.get(url)


if __name__ == '__main__':
    resp = upload_to_fileio('test.txt')
    link = get_link_from_resp(resp)
    pyperclip.copy(link)

