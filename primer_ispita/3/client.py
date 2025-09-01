from network import Client
import rsa


def handle_connection(socket):
    # Generate client RSA
    n, e, d = rsa.generate()

    # TODO: Implement client logic

    server_n, server_e = socket.recv()

    socket.send((n, e))

    m = 42

    c = rsa.encrypt(server_n, server_e, m)
    socket.send(c)

    c_reply = socket.recv()

    reply = rsa.decrypt(n, d, c_reply)
    print(f"Reply m: {reply}")


if __name__ == '__main__':
    Client(handle_connection).start()


