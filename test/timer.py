from datetime import datetime


def timer(func, repeat=1000000):
    before = datetime.now()
    for i in range(repeat):
        func()
    end = datetime.now()
    time = end - before
    round_time = time / repeat
    print("Total:", time, "Round:", round_time)
    return time
