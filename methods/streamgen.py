import random

import time


def large_stream(n):
    for _ in range(n):
        yield random.randint(1, 1000)


n = 1000000
for num in large_stream(n):
    print(num)
    time.sleep(1)
