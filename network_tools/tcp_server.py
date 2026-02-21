import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999



# server.bind((bind_ip, bind_port))
#
# server.listen(5)
#
# print("[*] Listening on %s:%d" % (bind_ip, bind_port))

def handle_client(client_socket):
    with client_socket as sock: # When the block exits, the socket closes automatically.
        request = sock.recv(1024)
        print("[*] Received: %s" % request)
        sock.send(b'ACK')
        print(client_socket.getpeername())
        # client_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((bind_ip, bind_port))
    server.listen(5)
    print(f'[*] Listening on {bind_ip}:{bind_port}')

    while True:
        client, addr = server.accept()
        print("[*] Accepted connection from: %s:%d" % (addr[0], addr[1]))
        # spin up our client thread to handle incoming data
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

if __name__ == '__main__':
    main()

