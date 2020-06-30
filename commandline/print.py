import sys


def print(*args, **kwargs):
    text = kwargs.get("sep", ' ').join(str(arg) for arg in args) + kwargs.get("end", '\n')
    kwargs.get("file", sys.stdout).write(text)
