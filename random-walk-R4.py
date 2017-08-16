# Random walk (R4: re-usable)
# Copyright (c) 2017 Nicolas P. Rougier and Fabien C.Y. Benureau
# Release under the BSD 2-clause license
# Tested with Python 3.6 / Numpy 1.12.0 / macOS 10.12.4 / 64 bits architecture
import random

def walk(x0=0, step=1, count=10, seed=0):
    """ Random walk 
        x0   : initial position (default 0)
        step : step size (default 1)
        count: number of steps (default 10)
        seed : seed for the initialization of the random generator (default 0)
    """
    x = x0
    path = []
    random.seed(seed)
    for i in range(count):
        if random.uniform(-1,+1) > 0:
            x = x + step
        else:
            x = x - step
        path.append(x)
    return path


if __name__ == '__main__':
    # Unit test checking reproducibility
    assert walk(0, 1, 10, 1) == [-1, 0, 1, 0, -1, -2, -1, 0, -1, -2]

    # Simulation parameters
    parameters = { 'x0':    0,
                   'step':  1,
                   'count': 10,
                   'seed' : 1 }
    path = walk(**parameters)
    results = {'data':  path, 'parameters': parameters}

    # Save & display results
    with open("results-R4.txt", "w") as fd:
        fd.write(str(results))

    print(path)
