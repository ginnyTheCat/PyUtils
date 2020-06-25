import random

from simalia.commandline import SocketCommandLine


def parse(cmd):
    if cmd[0] == "test":
        if len(cmd) != 3:
            line.print_code(1, 2)
        else:
            line.print(cmd[1] + ", " + cmd[2])
        return True
    return False


def quit():
    global running
    running = False


running = True
line = SocketCommandLine(parse, start_client=True, on_quit=quit)
line.start()

while running:
    print(random.randint(0, 1000))
