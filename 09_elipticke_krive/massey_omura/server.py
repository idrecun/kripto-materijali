import network
import massey_omura as mo
import os

def logic(socket):
    enc_key, dec_key = mo.generate_keys()

    # Receive the encrypted message from the client
    client_encrypted = socket.recv()

    # Encrypt using server's encryption key
    client_server_encrypted = mo.encrypt(enc_key, client_encrypted)
    socket.send(client_server_encrypted)

    # Receive the server-encrypted message from the client
    server_encrypted = socket.recv()
    decrypted = mo.decrypt(dec_key, server_encrypted)
    print(f'Message from client: ', mo.decode(decrypted))

server = network.Server(logic)
server.start()
