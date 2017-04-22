# Random walk (R3: reproducible)
# Copyright (c) 2017 Nicolas P. Rougier and Fabien C.Y. Benureau
# Release under the BSD 2-clause license
# Tested with Python 3.6 / macOS 10.12.4 / 64 bits architecture
import random
from itertools import accumulate

def walk(n):
    """ Random walk for n steps """

    steps = [-1 if random.uniform(-1,+1) < 0 else +1 for i in range(n)]
    return list(accumulate(steps))

if __name__ == '__main__':
    # Unit test
    random.seed(1)
    assert walk(10) == [-1, 0, 1, 0, -1, -2, -1, 0, -1, -2]

    # Random walk for 10 steps
    seed = 1
    random.seed(seed)
    x = walk(10)

    # Dipslay & ave results
    print(x)
    with open("results-R3-%d.txt" % seed, "w") as file:
        file.write(str(x))
