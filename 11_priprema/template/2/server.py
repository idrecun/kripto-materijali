import socket
import threading
import pickle
import rsa
import os

def handle_client(client_socket, address):
    try:
        username = client_socket.recv(1024).decode("utf-8")
        filename = username + ".pubkey"

        if not os.path.isfile(filename):
            print(f"Unknown user {username}. Requesting RSA public key from client...")
            client_socket.send(f"Unknown user {username}".encode("utf-8"))

            pub = pickle.loads(client_socket.recv(1024))
            with open(filename, "wb") as f:
                pickle.dump(pub, f)
            print(f"RSA public key saved to {filename}")

        print(f"Reading RSA public key from {filename}...")
        with open(filename, "rb") as f:
            pub = pickle.load(f)


    except Exception as e:
        print(f"Error handling client {address}: {e}")

    client_socket.close()
    print(f"Connection with {address[0]}:{address[1]} closed.")

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind((host, port))

    server_socket.listen(5)
    print(f"Server started on {host}:{port}")

    while True:
        client_socket, address = server_socket.accept()
        print(f"Accepted connection from {address[0]}:{address[1]}")

        client_handler = threading.Thread(target=handle_client, args=(client_socket, address))
        client_handler.start()

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 12345

    start_server(host, port)
