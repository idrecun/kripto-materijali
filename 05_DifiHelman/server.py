import socket
import threading
import diffie_hellman as dh

# Function to handle incoming messages from the client
def handle_client(client_socket, address):
    try:
        # Receive data from the client
        data = client_socket.recv(1024).decode("utf-8")

        print(f"Received public key from {address[0]}:{address[1]}: {data}")
        client_public_key = int(data, 16)

        private_key = dh.private_key()
        public_key  = dh.public_key(private_key)
        shared_key  = dh.shared_key(private_key, client_public_key)

        shared_key_hex = hex(shared_key)
        print(f"Shared secret key with {address[0]}:{address[1]}: {shared_key_hex}")

        public_key_hex = hex(public_key)
        client_socket.send(public_key_hex.encode("utf-8"))
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
