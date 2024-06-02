import socket
import threading
import ec
import diffie_hellman as dh
import massey_omura as mo
import os

# Function to handle incoming messages from the client
def handle_client(client_socket, address):
    try:
        enc_key, dec_key = mo.generate_keys()

        # Receive the encrypted message from the client
        data = client_socket.recv(1024).decode("utf-8")
        client_encrypted = ec.Point(ec.secp256k1, 0, 0)
        client_encrypted.hex_decode(data)

        # Encrypt using server's encryption key
        twice_encrypted = mo.encrypt(enc_key, client_encrypted)
        client_socket.send(twice_encrypted.hex_encode().encode("utf-8"))

        # Receive the server-encrypted message from the client
        data = client_socket.recv(1024).decode("utf-8")
        server_encrypted = ec.Point(ec.secp256k1, 0, 0)
        server_encrypted.hex_decode(data)

        decrypted = mo.decrypt(dec_key, server_encrypted)
        print(f'Message from client {address[0]}:{address[1]}: ', mo.decode(decrypted))

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
