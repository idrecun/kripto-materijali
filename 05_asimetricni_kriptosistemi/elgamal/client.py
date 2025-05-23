import sys
sys.path.append('..')

from network import Client
import diffie_hellman as dh
import elgamal
import bits

def handle_connection(socket):
    # Generate client's private and public keys
    client_private = dh.private_key()
    client_public = dh.public_key(client_private)
    
    # Receive server's public key
    server_public = socket.recv()
    
    # Send client's public key
    socket.send(client_public)
    
    # Send encrypted message
    message = "Hello server! This is a secret message using ElGamal encryption."
    message_bits = bits.bits_from_string(message)
    message_int = bits.bits_to_int(message_bits)
    encrypted_message = elgamal.encrypt(client_private, server_public, message_int)
    socket.send(encrypted_message)
    
    # Receive and decrypt response
    encrypted_response = socket.recv()
    decrypted_int = elgamal.decrypt(client_private, server_public, encrypted_response)
    decrypted_bits = bits.bits_from_int(decrypted_int, 8 * ((decrypted_int.bit_length() + 7) // 8))
    decrypted_response = bits.bits_to_string(decrypted_bits)
    print(f"Server response: {decrypted_response}")

if __name__ == '__main__':
    client = Client(handle_connection)
    print("ElGamal Client started. Connecting to server...")
    client.start() 