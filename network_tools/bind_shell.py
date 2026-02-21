import socket
import threading
import sys
import time

BIND_IP = "127.0.0.1" # localhost only
BIND_PORT = 9999

ALLOWED_COMMANDS = ["help", "echo", "time", "exit"]

def handle_client(client_socket):
    with client_socket as sock:
        sock.send(b"Bind shell lab ready. Type 'help'\n")

        while True:
            sock.send(b"> ")
            data = client_socket.recv(1024).decode()
            print("[*] Received: %s" % data)
            print(client_socket.getpeername())

            if not data:
                break

            command = data.decode().strip()
            if command == "help":
                response = (
                    "Allowed commands:\n"
                    "- help\n"
                    "- echo <text>\n"
                    "- time\n"
                    "- exit\n"
                )

            elif command.startswith("echo "):
                response = command[5:] + "\n"

            elif command == "time":
                response = time.ctime() + "\n"

            elif command == "exit":
                sock.send(b"Bye!\n")
                break

            else:
                response = "Command not allowed\n"

            sock.send(response.encode())

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((BIND_IP, BIND_PORT))
    server.listen(5)

    print(f"[+] Bind shell listening on {BIND_IP}:{BIND_PORT}")

    try:
        while True:
            client, addr = server.accept()
            print(f"[+] Connection from {addr[0]}:{addr[1]}")
            t = threading.Thread(target=handle_client, args=(client,))
            t.start()
    except KeyboardInterrupt:
        print("\n[C-c] Port forwarding stopped.")
        server.close()
        sys.exit(0)

if __name__ == "__main__":
    main()