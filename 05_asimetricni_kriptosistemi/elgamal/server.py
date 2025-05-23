import sys
sys.path.append('..')

from network import Server
import diffie_hellman as dh
import elgamal
import bits

def handle_connection(socket):
    # Generate server's private and public keys
    server_private = dh.private_key()
    server_public = dh.public_key(server_private)
    
    # Send server's public key
    socket.send(server_public)
    
    # Receive client's public key
    client_public = socket.recv()
    
    # Receive encrypted message
    encrypted_message = socket.recv()
    
    # Decrypt message
    decrypted_int = elgamal.decrypt(server_private, client_public, encrypted_message)
    decrypted_bits = bits.bits_from_int(decrypted_int, 8 * ((decrypted_int.bit_length() + 7) // 8))
    decrypted_message = bits.bits_to_string(decrypted_bits)
    print(f"Received message: {decrypted_message}")
    
    # Send encrypted response
    response = "Message received and decrypted successfully!"
    response_bits = bits.bits_from_string(response)
    response_int = bits.bits_to_int(response_bits)
    encrypted_response = elgamal.encrypt(server_private, client_public, response_int)
    socket.send(encrypted_response)

if __name__ == '__main__':
    server = Server(handle_connection)
    print("ElGamal Server started. Waiting for connections...")
    server.start() 