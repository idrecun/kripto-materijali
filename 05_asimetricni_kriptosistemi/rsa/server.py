import sys
sys.path.append('..')

from network import Server
import rsa
import bits

def handle_connection(socket):
    # Generate server's RSA keys
    n, enc_key, dec_key = rsa.generate()
    
    # Send server's public key (n, e)
    socket.send((n, enc_key))
    
    # Receive client's public key
    client_n, client_enc_key = socket.recv()
    
    # Receive encrypted message
    encrypted_message = socket.recv()
    
    # Decrypt message
    decrypted_message = rsa.decrypt(n, dec_key, encrypted_message)
    message_str = bits.bits_to_string(bits.bits_from_int(decrypted_message, 8 * ((decrypted_message.bit_length() + 7) // 8)))
    print(f"Received message: {message_str}")
    
    # Send encrypted response
    response = "Message received and decrypted successfully!"
    response_bits = bits.bits_from_string(response)
    response_int = bits.bits_to_int(response_bits)
    encrypted_response = rsa.encrypt(client_n, client_enc_key, response_int)
    socket.send(encrypted_response)

if __name__ == '__main__':
    server = Server(handle_connection)
    print("RSA Server started. Waiting for connections...")
    server.start() 