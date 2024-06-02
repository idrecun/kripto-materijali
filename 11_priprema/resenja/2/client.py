import socket
import threading
import pickle
import rsa
import os

# Function to start the client
def start_client(host, port):
    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        username = input("Username: ")
        filename = username + ".keys"

        if not os.path.isfile(filename):
            print(f"Keys not found. Generating new RSA keys...")
            priv, pub = rsa.generateKeyPair()

            with open(filename, "wb") as f:
                pickle.dump((priv, pub), f)
            print(f"RSA keys saved to {filename}")

        print(f"Reading RSA keys from {filename}...")
        with open(filename, "rb") as f:
            priv, pub = pickle.load(f)

        # Connect to the server
        client_socket.connect((host, port))
        print(f"Connected to server {host}:{port}")

        print(f"Signing in as {username}")
        client_socket.send(username.encode("utf-8"))

        response = client_socket.recv(1024).decode("utf-8")
        if response == f"Unknown user {username}":
            print(f"Server: {response}")
            print(f"Registering public key with server...")
            client_socket.send(pickle.dumps(pub))
            response = client_socket.recv(1024).decode("utf-8")
        
        print(f"Received message {response} for authentication")

        signature = rsa.sign(priv, pub, int(response, 10))
        client_socket.send(pickle.dumps(signature))

        response = client_socket.recv(1024).decode("utf-8")
        print(f"Server: {response}")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the socket
        client_socket.close()
        print("Connection closed.")

if __name__ == "__main__":
    # Host and port
    host = "127.0.0.1"
    port = 12345

    # Start client
    start_client(host, port)

