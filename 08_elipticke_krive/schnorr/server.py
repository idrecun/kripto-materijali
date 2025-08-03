from network import Server
import schnorr

def handle_connection(socket):
    # Generate server's keypair
    server_private, server_public = schnorr.generate()
    
    # Send server's public key
    socket.send(server_public)
    
    # Receive client's public key
    client_public = socket.recv()
    
    # Receive signed message
    message, signature = socket.recv()
    
    # Verify signature
    is_valid = schnorr.verify(client_public, message, signature)
    print(f"Received message: {message}")
    print(f"Signature is valid: {is_valid}")
    
    # Send signed response
    response = "Message and signature received and verified!"
    response_signature = schnorr.sign(server_private, response)
    socket.send((response, response_signature))

if __name__ == '__main__':
    server = Server(handle_connection)
    print("Schnorr Server started. Waiting for connections...")
    server.start() 