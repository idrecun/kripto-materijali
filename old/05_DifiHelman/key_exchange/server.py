import network
import diffie_hellman as dh

def logic(socket):
    # Generate DH key pair
    private_key = dh.private_key()
    public_key  = dh.public_key(private_key)

    # Receive client's public key from the client
    client_public_key = socket.recv()
    print(f"Received public key from client: {hex(client_public_key)}")

    # Calculated shared key
    shared_key  = dh.shared_key(private_key, client_public_key)
    print(f"Shared secret key with client: {hex(shared_key)}")

    # Send server's public key to the client
    socket.send(public_key)

server = network.Server(logic)
server.start()
