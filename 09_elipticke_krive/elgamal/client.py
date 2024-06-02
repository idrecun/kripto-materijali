import network
import diffie_hellman as dh
import elgamal

def logic(socket):
    # Receive public key from the server
    server_public_key = socket.recv()

    while True:
        private_key = dh.private_key()
        public_key  = dh.public_key(private_key)

        message = input('Enter message to send to the server: ')
        encoded_message = elgamal.encode(message)
        ciphertext = elgamal.encrypt(private_key, server_public_key, encoded_message)

        # Send public key and ciphertext to the server
        socket.send((public_key, ciphertext))

client = network.Client(logic)
client.start()
