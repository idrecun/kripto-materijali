from network import Client
import ecdsa

def handle_connection(socket):
    # Generate client's keypair
    client_private, client_public = ecdsa.generate()
    
    # Receive server's public key
    server_public = socket.recv()
    
    # Send client's public key
    socket.send(client_public)
    
    # Send signed message
    message = "Hello server! This message is signed with EC-DSA."
    signature = ecdsa.sign(client_private, message)
    socket.send((message, signature))
    
    # Receive and verify response
    response, response_signature = socket.recv()
    is_valid = ecdsa.verify(server_public, response, response_signature)
    print(f"Server response: {response}")
    print(f"Response signature is valid: {is_valid}")

if __name__ == '__main__':
    client = Client(handle_connection)
    print("EC-DSA Client started. Connecting to server...")
    client.start() 