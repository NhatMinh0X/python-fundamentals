import socket
import ssl

target_host = "www.google.com"
target_port = 443

# 1. create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. crate a ssl context
context = ssl.create_default_context()

# 3. Wrap sockets with TLS
secure_sock = context.wrap_socket(
    sock,
    server_hostname=target_host  # SNI - extremely important! -- Modern HTTPS uses SNI (Server Name Indication).
)

# 4. connect
secure_sock.connect((target_host, target_port))

# 5. send some HTTP request
request = (
    "GET / HTTP/1.1\r\n"
    f"Host: {target_host}\r\n"
    "User-Agent: Python-HTTPS-Socket\r\n"
    "Connection: close\r\n"
    "\r\n"
)

secure_sock.sendall(request.encode())

# 6. Received all response
response = b""
while True:
    data = secure_sock.recv(4096)
    if not data:
        break
    response += data

# 7. close
secure_sock.close()

# 8. print result
print(response.decode(errors="ignore"))