import sys
sys.path.append('..')

from network import Client
import dsa

def handle_connection(socket):
    # Generate client's keys
    private_key, public_key = dsa.generate()
    
    # Receive server's public key
    server_public_key = socket.recv()
    
    # Send client's public key
    socket.send(public_key)
    
    # Send signed message
    message = "Hello server! This message is signed with DSA."
    signature = dsa.sign(private_key, message)
    socket.send((message, signature))
    
    # Receive and verify response
    response, response_signature = socket.recv()
    is_valid = dsa.verify(server_public_key, response, response_signature)
    print(f"Server response: {response}")
    print(f"Response signature is valid: {is_valid}")

if __name__ == '__main__':
    client = Client(handle_connection)
    print("DSA Client started. Connecting to server...")
    client.start() 