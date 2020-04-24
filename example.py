from commandline import *


def parse(cmd):
    if cmd[0] == "test":
        if len(cmd) != 3:
            line.print_code(1, 2)
        else:
            line.print(cmd[1] + ", " + cmd[2])
        return True
    return False


line = SocketCommandLine(parse, start_client=True)
line.start()
