from datetime import datetime


def timer(func, repeat=1000000):
    before = datetime.now()
    for i in range(repeat):
        func()
    end = datetime.now()
    return end - before
