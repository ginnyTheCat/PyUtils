import os
import socket
import terminal
from threading import Thread

ENCODING = 'utf-8'


class _CommandLine(Thread):

    def __init__(self, parser, on_quit=None):
        super().__init__()
        self.stop = False
        self.parser = parser
        self.on_quit = on_quit

    def _raw_parse(self, cmd):
        cmd = cmd.lower().strip()
        if cmd == "":
            return True
        args = cmd.split(" ")
        if not self.parse(args):
            self.print_code(0)

    def parse(self, args):
        if self.parser(args):
            return True
        elif args[0] == "kill":
            os._exit(0)
            return True
        elif args[0] == "quit" or args[0] == "exit":
            if self.on_quit:
                self.on_quit()
            self.stop = True
            return True
        return False

    def print_code(self, code, data=None):
        if code == 0:
            self.print("No such command")
        elif code == 1:
            self.print("Needs " + str(data) + " args")

    def print(self, text):
        pass


class NativeCommandLine(_CommandLine):

    def run(self):
        while not self.stop:
            self._raw_parse(input("> "))

    def print(self, text):
        print(text)


class SocketCommandLine(_CommandLine):

    def __init__(self, parser, on_quit=None, port=2300, start_client=False):
        super().__init__(parser, self.__quit)
        self.__on_quit = on_quit
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client = None
        self.start_client = start_client
        self.port = port

    def __quit(self):
        self.client.sendall(0x04.to_bytes(1, 'big'))
        self.socket.close()
        if self.__on_quit:
            self.__on_quit()

    def __connect(self):
        self.socket.listen(1)
        self.client, _ = self.socket.accept()
        print("Connected")

    def run(self):
        print("Waiting for connection on port " + str(self.port))
        self.socket.bind(("127.0.0.1", self.port))
        terminal.start_python_script("socket_client.py")
        self.__connect()
        while not self.stop:
            try:
                data = self.client.recv(4096)
                self._raw_parse(data.decode(ENCODING))
            except ConnectionResetError:
                print("Disconnected")
                print("Waiting for connection")
                self.__connect()

    def print(self, text):
        self.client.sendall(text.encode(ENCODING))
