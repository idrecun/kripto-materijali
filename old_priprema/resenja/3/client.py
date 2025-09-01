import socket
import threading
import pickle
import massey_omura as mo
import ec

# Function to start the client
def start_client(host, port):
    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((host, port))
        print(f"Connected to server {host}:{port}")

        enc, dec = mo.generateKeyPair()

        message = int(input("Number: "))
        M = ec.secp256k1.encode_message(message)

        MClient = mo.encrypt(enc, M)
        client_socket.send(pickle.dumps(MClient))

        MClientServer = pickle.loads(client_socket.recv(1024))
        MServer = mo.decrypt(dec, MClientServer)
        client_socket.send(pickle.dumps(MServer))

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

