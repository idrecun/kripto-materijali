import sys
sys.path.append('..')

from network import Client
import diffie_hellman as dh
import bits

def handle_connection(socket):
    # Generate client's private and public keys
    client_private = dh.private_key()
    client_public = dh.public_key(client_private)
    
    # Receive server's public key
    server_public = socket.recv()
    
    # Send client's public key
    socket.send(client_public)
    
    # Calculate shared secret
    shared_secret = dh.shared_key(client_private, server_public)
    print(f"Shared secret established: {shared_secret}")
    
    # Send an encrypted test message
    message = "Hello, server! This is a secret message."
    message_bits = bits.bits_from_string(message)
    message_int = bits.bits_to_int(message_bits)
    encrypted_message = message_int ^ shared_secret
    socket.send(encrypted_message)
    
    # Receive and decrypt confirmation
    encrypted_confirmation = socket.recv()
    decrypted_int = encrypted_confirmation ^ shared_secret
    decrypted_bits = bits.bits_from_int(decrypted_int, 8 * ((decrypted_int.bit_length() + 7) // 8))
    decrypted_confirmation = bits.bits_to_string(decrypted_bits)
    print(f"Server response: {decrypted_confirmation}")

if __name__ == '__main__':
    client = Client(handle_connection)
    print("DH Client started. Connecting to server...")
    client.start() 