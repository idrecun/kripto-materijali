import sys
sys.path.append('..')

from network import Client
import rsa_sign

def handle_connection(socket):
    # Generate client's keypair
    private_key, public_key = rsa_sign.generate_keypair()
    
    # Receive server's public key
    server_public_key = socket.recv()
    
    # Send client's public key
    socket.send(public_key)
    
    # Send signed message
    message = "Hello server! This message is signed with RSA."
    signature = rsa_sign.sign(private_key, message)
    socket.send((message, signature))
    
    # Receive and verify response
    response, response_signature = socket.recv()
    is_valid = rsa_sign.verify(server_public_key, response, response_signature)
    print(f"Server response: {response}")
    print(f"Response signature is valid: {is_valid}")

if __name__ == '__main__':
    client = Client(handle_connection)
    print("RSA Signature Client started. Connecting to server...")
    client.start() 