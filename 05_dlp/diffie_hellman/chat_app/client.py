import network
import diffie_hellman as dh

def logic(socket):
    while True:
        # Generate DH key pair
        private_key = dh.private_key()
        public_key  = dh.public_key(private_key)

        # Send public key to the server
        socket.send(public_key)

        # Receive public key from the server
        server_public_key = socket.recv()
        
        # Calculate shared key
        shared_key = dh.shared_key(private_key, server_public_key)

        # Encrypt message using AES and send it to the server
        message = input("Enter message to send (or 'quit' to exit): ")
        if message.lower() == 'quit':
            break

        # encrypted_message = aes.encrypt(shared_key, message)
        encrypted_message = message
        socket.send(encrypted_message)

client = network.Client(logic)
client.start()
