import socket

HOST = "127.0.0.1"
PORT = 4444

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)
print(f"[+] Listening on {HOST}:{PORT}")
client, addr = server.accept()
print(f"[+] Connection from {addr}")

while True:
    cmd = input("shell> ")
    if cmd.strip() == "":
        continue
    client.send((cmd + "\n").encode())

    if cmd.strip() == "exit":
        break

    data = b""
    while True:
        chunk = client.recv(4096)
        if len(chunk) < 4096:
            data += chunk
            break
        data += chunk

    print(data.decode(errors="ignore"))

client.close()
server.close()