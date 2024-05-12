import socket
import threading
import diffie_hellman as dh
import massey_omura as mo

# Function to start the client
def start_client(host, port):
    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        client_socket.connect((host, port))

        enc_key, dec_key = mo.generate_keys()

        message = input('Enter message to send to the server: ')
        encoded_message = mo.encode(message)

        # Encrypt using client's encryption key
        client_encrypted = mo.encrypt(enc_key, encoded_message)
        client_encrypted_hex = hex(client_encrypted)
        client_socket.send(client_encrypted_hex.encode("utf-8"))

        # Receive message encrypted using server's encryption key
        response = client_socket.recv(1024).decode("utf-8")
        twice_encrypted = int(response, 16)

        # Decrypt using client's decryption key
        server_encrypted = mo.decrypt(dec_key, twice_encrypted)
        server_encrypted_hex = hex(server_encrypted)
        client_socket.send(server_encrypted_hex.encode("utf-8"))

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

