import sys
sys.path.append('..')

from network import Client
import rsa_sign

def handle_connection(socket):
    # Generate client's keys
    n, verify_key, sign_key = rsa_sign.generate()
    
    # Receive server's public key
    server_n, server_verify_key = socket.recv()
    
    # Send client's public key
    socket.send((n, verify_key))
    
    # Send signed message
    message = "Hello server! This message is signed with RSA."
    signature = rsa_sign.sign(n, sign_key, message)
    socket.send((message, signature))
    
    # Receive and verify response
    response, response_signature = socket.recv()
    is_valid = rsa_sign.verify(server_n, server_verify_key, response, response_signature)
    print(f"Server response: {response}")
    print(f"Response signature is valid: {is_valid}")

if __name__ == '__main__':
    client = Client(handle_connection)
    print("RSA Signature Client started. Connecting to server...")
    client.start() 