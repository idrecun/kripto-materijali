import sys
sys.path.append('..')

from network import Client
import schnorr

def handle_connection(socket):
    # Generate client's keypair
    client_private = schnorr.private_key()
    client_public = schnorr.public_key(client_private)
    
    # Receive server's public key
    server_public = socket.recv()
    
    # Send client's public key
    socket.send(client_public)
    
    # Send signed message
    message = "Hello server! This message is signed with Schnorr."
    signature = schnorr.sign(client_private, message)
    socket.send((message, signature))
    
    # Receive and verify response
    response, response_signature = socket.recv()
    is_valid = schnorr.verify(server_public, response, response_signature)
    print(f"Server response: {response}")
    print(f"Response signature is valid: {is_valid}")

if __name__ == '__main__':
    client = Client(handle_connection)
    print("Schnorr Client started. Connecting to server...")
    client.start() 