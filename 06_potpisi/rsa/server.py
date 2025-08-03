import sys
sys.path.append('..')

from network import Server
import rsa_sign

def handle_connection(socket):
    # Generate server's keys
    n, verify_key, sign_key = rsa_sign.generate()
    
    # Send server's public key (n, verify_key)
    socket.send((n, verify_key))
    
    # Receive client's public key
    client_n, client_verify_key = socket.recv()
    
    # Receive signed message
    message, signature = socket.recv()
    
    # Verify signature
    is_valid = rsa_sign.verify(client_n, client_verify_key, message, signature)
    print(f"Received message: {message}")
    print(f"Signature is valid: {is_valid}")
    
    # Send signed response
    response = "Message and signature received and verified!"
    response_signature = rsa_sign.sign(n, sign_key, response)
    socket.send((response, response_signature))

if __name__ == '__main__':
    server = Server(handle_connection)
    print("RSA Signature Server started. Waiting for connections...")
    server.start() 