import network
import diffie_hellman as dh

def logic(socket):
    while True:
        # Generate DH key pair
        private_key = dh.private_key()
        public_key  = dh.public_key(private_key)

        # Receive public key from the client
        client_public_key = socket.recv()

        # Calculate shared key
        shared_key = dh.shared_key(private_key, client_public_key)

        # Send public key to the client
        socket.send(public_key)

        # Receive message from the client
        message = socket.recv()
        if not message:
            break

        # decrypted_message = aes.decrypt(shared_key, data).decode('utf-8')
        decrypted_message = message 
        print(f"Received message from client: {decrypted_message}")

server = network.Server(logic)
server.start()
