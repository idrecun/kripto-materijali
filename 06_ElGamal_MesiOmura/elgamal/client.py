import socket
import threading
import diffie_hellman as dh
import elgamal

# Function to start the client
def start_client(host, port):
    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        client_socket.connect((host, port))

        # Receive public key from the server
        response = client_socket.recv(1024).decode("utf-8")
        server_public_key = int(response, 16)

        while True:
            private_key = dh.private_key()
            public_key  = dh.public_key(private_key)
            # shared_key = dh.shared_key(private_key, server_public_key)

            message = input('Enter message to send to the server: ')
            encoded_message = elgamal.encode(message)
            ciphertext = elgamal.encrypt(private_key, server_public_key, encoded_message)

            public_key_hex = hex(public_key)
            ciphertext_hex = hex(ciphertext)
            payload = public_key_hex + ":" + ciphertext_hex

            # Send public key to the server
            client_socket.send(payload.encode("utf-8"))

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

