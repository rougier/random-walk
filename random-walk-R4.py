# Random walk (R4: re-usable)
# Copyright (c) 2017 Nicolas P. Rougier and Fabien C.Y. Benureau
# Release under the BSD 2-clause license
# Tested with CPython 3.6.2 / macOS 10.12.6 / 64 bits architecture
import sys, subprocess, datetime, random

def generate_walk(count, x0=0, step=1, seed=0):
    """ Random walk
        count: number of steps
        x0   : initial position (default 0)
        step : step size (default 1)
        seed : seed for the initialization of the random generator (default 0)
    """
    random.seed(seed)
    x = x0
    walk = []
    for i in range(count):
        if random.uniform(-1, +1) > 0:
            x += 1
        else:
            x -= 1
        walk.append(x)
    return walk

def generate_results(count, x0=0, step=1, seed=0):
    """Compute a walk and return it alongside its context"""
    # If repository is dirty, don't do anything
    if subprocess.call(('git', 'diff-index', '--quiet', 'HEAD')):
        print('Repository is dirty, please commit first')
        sys.exit(1)

    # Get git hash if any
    revision = subprocess.check_output(('git', 'rev-parse', 'HEAD'))

    # Compute results
    walk = generate_walk(count=count, x0=x0, step=step, seed=seed)
    return {'data'      : walk,
            'parameters': {'x0':x0, 'step':step, 'count':count, 'seed':seed},
            'timestamp' : str(datetime.datetime.utcnow()),
            'revision'  : revision,
            'system'    : sys.version}

if __name__ == '__main__':
    # Unit test checking reproducibility (will fail with Python<=3.2)
    assert generate_walk(10, 0, 1, 42) == [1, 0, -1, -2, -1, 0, 1, 0, -1, -2]

    # Simulation parameters
    count, x0, seed = 10, 0, 1
    results = generate_results(count, x0=x0, seed=seed)

    # Save & display results
    with open('results-R4.txt', 'w') as fd:
        fd.write(str(results))
    print(results['data'])
