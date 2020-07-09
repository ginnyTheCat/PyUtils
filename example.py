from simalia.math import *
from simalia.recommended import *


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


"""running = True
line = SocketCommandLine(parse, start_client=True, on_quit=quit)
line.start()

while running:
    print(random.randint(0, 1000))"""

x = -n(1) / (n(10) % n(6) - n(-5) * n(100) / n(30) ** n(3))
print(x)
res = x.calc()
print()
print(res.latex())
print(res)

pi = Pi(5)
sin = Sine(n(10))
print()
print(pi, "=", pi.calc())
print(sin, "=", sin.calc())
