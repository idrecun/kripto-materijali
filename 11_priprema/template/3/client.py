import socket
import threading
import pickle
import ec

def start_client(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
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

