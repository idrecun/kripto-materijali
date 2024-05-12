import socket
import threading
import diffie_hellman as dh

# Function to start the client
def start_client(host, port):
    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        client_socket.connect((host, port))
        print(f"Connected to server {host}:{port}")

        while True:
            private_key = dh.private_key()
            public_key  = dh.public_key(private_key)
            public_key_hex = hex(public_key)

            # Send public key to the server
            client_socket.send(public_key_hex.encode("utf-8"))

            # Receive public key from the server
            response = client_socket.recv(1024).decode("utf-8")
            print(f"Received public key from server: {response}")

            server_public_key = int(response, 16)
            shared_key = dh.shared_key(private_key, server_public_key)
            shared_key_hex = hex(shared_key)
            print(f"Shared key with server: {shared_key_hex}")

            # Send data to the server
            message = input("Enter message to send (or 'quit' to exit): ")
            if message.lower() == 'quit':
                break
            encrypted_message = aes.encrypt(shared_key, message.encode("utf-8"))
            client_socket.send(encrypted_message)

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

