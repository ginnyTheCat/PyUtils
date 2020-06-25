from threading import Thread
import socket

ENCODING = 'utf-8'


class SocketCommandLineClient(Thread):

    def __init__(self, port=2300):
        super().__init__()
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client = None
        self.stop = False
        self.port = port

    def run(self):
        print("Connection to server on port " + str(self.port))
        self.server.connect(("127.0.0.1", self.port))
        while not self.stop:
            text = input("> ")
            self.server.sendall(text.encode(ENCODING))
            data = self.server.recv(4096)
            if int.from_bytes(data, 'big') == 0x04:
                self.stop = True
            else:
                print(data.decode(ENCODING))


if __name__ == "__main__":
    client = SocketCommandLineClient()
    client.run()
