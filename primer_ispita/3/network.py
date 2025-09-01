import socket
import pickle


class Socket:
    def __init__(self, s):
        self.s = s

    def send(self, data):
        self.s.send(pickle.dumps(data))

    def recv(self):
        data = self.s.recv(4096)
        if not data:
            return None
        else:
            return pickle.loads(data)


class Client:
    def __init__(self, hook):
        self.host = '127.0.0.1'
        self.port = 12346
        self.hook = hook

    def start(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            client_socket.connect((self.host, self.port))
            self.hook(Socket(client_socket))
        except Exception as e:
            print(f'Error: {e}')
        finally:
            client_socket.close()


class Server:
    def __init__(self, hook):
        self.host = '127.0.0.1'
        self.port = 12346
        self.hook = hook

    def start(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((self.host, self.port))

        server_socket.listen()
        while True:
            client_socket, address = server_socket.accept()
            try:
                self.hook(Socket(client_socket))
            except Exception as e:
                print(f'Error: {e}')
            finally:
                client_socket.close()


