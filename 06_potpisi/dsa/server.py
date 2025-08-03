import sys
sys.path.append('..')

from network import Server
import dsa

def handle_connection(socket):
    # Generate server's keys
    private_key, public_key = dsa.generate()
    
    # Send server's public key
    socket.send(public_key)
    
    # Receive client's public key
    client_public_key = socket.recv()
    
    # Receive signed message
    message, signature = socket.recv()
    
    # Verify signature
    is_valid = dsa.verify(client_public_key, message, signature)
    print(f"Received message: {message}")
    print(f"Signature is valid: {is_valid}")
    
    # Send signed response
    response = "Message and signature received and verified!"
    response_signature = dsa.sign(private_key, response)
    socket.send((response, response_signature))

if __name__ == '__main__':
    server = Server(handle_connection)
    print("DSA Server started. Waiting for connections...")
    server.start() 