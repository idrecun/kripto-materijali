import network
import pickle
import diffie_hellman as dh
import elgamal
import os

def logic(socket):
    global private_key, public_key

    # Send the public key to the client
    socket.send(public_key)

    while True:
        # Receive public key and ciphertext from the client
        client_public_key, ciphertext = socket.recv()

        message = elgamal.decrypt(private_key, client_public_key, ciphertext)
        print(f'Message from client: ', elgamal.decode(message))

# Generate private key if 'server.key' not found
if not os.path.exists('server.key'):
    private_key = dh.private_key()
    with open('server.key', 'wb') as key_file:
        pickle.dump(private_key, key_file)

# Read private key from 'server.key'
with open('server.key', 'rb') as key_file:
    private_key = pickle.load(key_file)
    public_key = dh.public_key(private_key)

server = network.Server(logic)
server.start()
