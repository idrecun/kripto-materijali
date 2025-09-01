from network import Server
import rsa


def handle_connection(socket):
    # Generate server RSA
    n, e, d = rsa.generate()

    # TODO: Implement server logic

    socket.send((n, e))

    client_n, client_e = socket.recv()

    c = socket.recv()

    m = rsa.decrypt(n, d, c)
    print(f"Received m: {m}")

    reply = m + 1
    c_reply = rsa.encrypt(client_n, client_e, reply)
    socket.send(c_reply)


if __name__ == '__main__':
    Server(handle_connection).start()


