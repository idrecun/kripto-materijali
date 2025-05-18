import network
import diffie_hellman as dh

def logic(socket):
    private_key = dh.private_key()
    public_key  = dh.public_key(private_key)

    # Send public key to the server
    socket.send(public_key)

    # Receive public key from the server
    server_public_key = socket.recv()

    shared_key = dh.shared_key(private_key, server_public_key)
    shared_key_hex = hex(shared_key)
    print(f"Shared key with server: {shared_key_hex}")

    # Encrypt and send the file
    # Read and encrypt the whole file
    with open("large.txt", "rb") as file:
        file_data = file.read()
        encrypted_file = aes.encrypt(shared_key, file_data)

    # Send encrypted file data in chunks
    socket.sendall(encrypted_file)

client = network.Client(logic)
client.start()
