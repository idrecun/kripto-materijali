import socket
import threading
import pickle
import rsa
import os

def start_client(host, port):
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

        client_socket.connect((host, port))
        print(f"Connected to server {host}:{port}")

        # Implement me

    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()
        print("Connection closed.")

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 12345

    start_client(host, port)

