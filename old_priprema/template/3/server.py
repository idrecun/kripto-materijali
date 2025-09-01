import socket
import threading
import pickle
import ec

def handle_client(client_socket, address):
    try:
        # Implement me

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
