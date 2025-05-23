import sys
sys.path.append('..')

from network import Server
import diffie_hellman as dh
import bits

def handle_connection(socket):
    # Generate server's private and public keys
    server_private = dh.private_key()
    server_public = dh.public_key(server_private)
    
    # Send server's public key
    socket.send(server_public)
    
    # Receive client's public key
    client_public = socket.recv()
    
    # Calculate shared secret
    shared_secret = dh.shared_key(server_private, client_public)
    print(f"Shared secret established: {shared_secret}")
    
    # Receive and decrypt a test message
    encrypted_message = socket.recv()
    decrypted_int = encrypted_message ^ shared_secret
    decrypted_bits = bits.bits_from_int(decrypted_int, 8 * ((decrypted_int.bit_length() + 7) // 8))
    decrypted_message = bits.bits_to_string(decrypted_bits)
    print(f"Received message: {decrypted_message}")
    
    # Send back confirmation
    confirmation = "Message received successfully!"
    confirmation_bits = bits.bits_from_string(confirmation)
    confirmation_int = bits.bits_to_int(confirmation_bits)
    encrypted_confirmation = confirmation_int ^ shared_secret
    socket.send(encrypted_confirmation)

if __name__ == '__main__':
    server = Server(handle_connection)
    print("DH Server started. Waiting for connections...")
    server.start() 