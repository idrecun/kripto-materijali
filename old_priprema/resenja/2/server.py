import socket
import threading
import pickle
import rsa
import os

# Function to handle incoming messages from the client
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

        message = "123"
        client_socket.send(message.encode("utf-8"))

        signature = pickle.loads(client_socket.recv(1024))
        if rsa.verify(pub, signature, int(message, 10)):
            response = "Authentication successful"
        else:
            response = "Authentication failed"
        client_socket.send(response.encode("utf-8"))
        print(response)

    except Exception as e:
        print(f"Error handling client {address}: {e}")

    # Close the client socket
    client_socket.close()
    print(f"Connection with {address[0]}:{address[1]} closed.")

# Function to start the server
def start_server(host, port):
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the host and port
    server_socket.bind((host, port))

    # Listen for incoming connections
    server_socket.listen(5)
    print(f"Server started on {host}:{port}")

    while True:
        # Accept incoming connection
        client_socket, address = server_socket.accept()
        print(f"Accepted connection from {address[0]}:{address[1]}")

        # Create a new thread to handle the client
        client_handler = threading.Thread(target=handle_client, args=(client_socket, address))
        client_handler.start()

if __name__ == "__main__":
    # Host and port
    host = "127.0.0.1"
    port = 12345

    # Start server
    start_server(host, port)
