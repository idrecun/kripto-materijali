import network
import diffie_hellman as dh
import massey_omura as mo

def logic(socket):
        enc_key, dec_key = mo.generate_keys()

        message = input('Enter message to send to the server: ')
        encoded_message = mo.encode(message)

        # Encrypt using client's encryption key
        client_encrypted = mo.encrypt(enc_key, encoded_message)
        socket.send(client_encrypted)

        # Receive message encrypted using server's encryption key
        client_server_encrypted = socket.recv()

        # Decrypt using client's decryption key
        server_encrypted = mo.decrypt(dec_key, client_server_encrypted)
        socket.send(server_encrypted)

client = network.Client(logic)
client.start()
