import network
import diffie_hellman as dh

def logic(socket):
    # Generate DH key pairs
    private_key = dh.private_key()
    public_key  = dh.public_key(private_key)

    # Send client's public key to the server
    socket.send(public_key)

    # Receive server's public key from the server
    server_public_key = socket.recv()
    print(f"Received public key from server: {hex(server_public_key)}")

    # Calculate shared key
    shared_key = dh.shared_key(private_key, server_public_key)
    print(f"Shared key with server: {hex(shared_key)}")

client = network.Client(logic)
client.start()
