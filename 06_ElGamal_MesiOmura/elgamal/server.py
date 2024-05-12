import socket
import threading
import diffie_hellman as dh
import elgamal
import os

# Function to handle incoming messages from the client
def handle_client(client_socket, address):
    global private_key, public_key

    try:
        # Send the public key to the client
        public_key_hex = hex(public_key)
        client_socket.send(public_key_hex.encode("utf-8"))

        while True:
            # Receive data from the client
            data = client_socket.recv(1024).decode("utf-8")
            client_public_key, ciphertext = [int(part, 16) for part in data.split(':')]

            # shared_key = dh.shared_key(private_key, client_public_key)
            message = elgamal.decrypt(private_key, client_public_key, ciphertext)
            
            print(f'Message from client {address[0]}:{address[1]}: ', elgamal.decode(message))

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
    global private_key, public_key

    # Host and port
    host = "127.0.0.1"
    port = 12345

    # Generate private key if 'server.key' not found
    if not os.path.exists('server.key'):
        private_key = dh.private_key()
        with open('server.key', 'w') as key_file:
            key_file.write(hex(private_key)[2:])

    # Read private key from 'server.key'
    with open('server.key', 'r') as key_file:
        key_hex = key_file.read()
        private_key = int(key_hex, 16)
        public_key = dh.public_key(private_key)

    # Start server
    start_server(host, port)
