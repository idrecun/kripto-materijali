from network import Server
import ecdsa

def handle_connection(socket):
    # Generate server's keypair
    server_private, server_public = ecdsa.generate()
    
    # Send server's public key
    socket.send(server_public)
    
    # Receive client's public key
    client_public = socket.recv()
    
    # Receive signed message
    message, signature = socket.recv()
    
    # Verify signature
    is_valid = ecdsa.verify(client_public, message, signature)
    print(f"Received message: {message}")
    print(f"Signature is valid: {is_valid}")
    
    # Send signed response
    response = "Message and signature received and verified!"
    response_signature = ecdsa.sign(server_private, response)
    socket.send((response, response_signature))

if __name__ == '__main__':
    server = Server(handle_connection)
    print("EC-DSA Server started. Waiting for connections...")
    server.start() 