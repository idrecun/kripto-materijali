import sys
sys.path.append('..')

from network import Client
import schnorr

def handle_connection(socket):
    # Receive server's public key
    server_public_key = socket.recv()
    
    # Generate client's keypair
    private_key, public_key = schnorr.generate()
    
    # Send client's public key
    socket.send(public_key)
    
    # Send signed message
    message = "Hello server! This message is signed with Schnorr."
    signature = schnorr.sign(private_key, message)
    socket.send((message, signature))
    
    # Receive and verify response
    response, response_signature = socket.recv()
    is_valid = schnorr.verify(server_public_key, response, response_signature)
    print(f"Server response: {response}")
    print(f"Response signature is valid: {is_valid}")

if __name__ == '__main__':
    client = Client(handle_connection)
    print("Schnorr Client started. Connecting to server...")
    client.start() 