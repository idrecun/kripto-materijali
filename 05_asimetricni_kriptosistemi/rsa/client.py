import sys
sys.path.append('..')

from network import Client
import rsa
import bits

def handle_connection(socket):
    # Generate client's RSA keys
    n, enc_key, dec_key = rsa.generate()
    
    # Receive server's public key
    server_n, server_enc_key = socket.recv()
    
    # Send client's public key
    socket.send((n, enc_key))
    
    # Send encrypted message
    message = "Hello server! This is a secret message using RSA encryption."
    message_bits = bits.bits_from_string(message)
    message_int = bits.bits_to_int(message_bits)
    encrypted_message = rsa.encrypt(server_n, server_enc_key, message_int)
    socket.send(encrypted_message)
    
    # Receive and decrypt response
    encrypted_response = socket.recv()
    decrypted_response = rsa.decrypt(n, dec_key, encrypted_response)
    response_str = bits.bits_to_string(bits.bits_from_int(decrypted_response, 8 * ((decrypted_response.bit_length() + 7) // 8)))
    print(f"Server response: {response_str}")

if __name__ == '__main__':
    client = Client(handle_connection)
    print("RSA Client started. Connecting to server...")
    client.start() 