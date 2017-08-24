# Random walk (R5: replicable)
# Copyright (c) 2017 Nicolas P. Rougier and Fabien C.Y. Benureau
# Release under the BSD 2-clause license
# Tested with CPython 3.6.2 / NumPy 1.12.0 / macOS 10.12.6 / 64 bits architecture
import random
import numpy as np

def _rng(seed):
    """ Return a numpy random number generator initialized with seed
        as it would be with python random generator.
    """
    rng = random.Random()
    rng.seed(seed)
    _, keys, _ = rng.getstate()
    rng = np.random.RandomState()
    state = rng.get_state()
    rng.set_state((state[0], keys[:-1], state[2], state[3], state[4]))
    return rng

def walk(n, seed):
    """ Random walk for n steps """

    rng = _rng(seed)
    steps = 2*(rng.uniform(-1,+1,n) > 0) - 1
    return steps.cumsum().tolist()

if __name__ == '__main__':
    # Unit test
    assert walk(n=10, seed=42) == [1, 0, -1, -2, -1, 0, 1, 0, -1, -2]

    # Random walk for 10 steps, initialization with seed=1
    seed = 1
    path = walk(n=10, seed=seed)

    # Save & display results
    results = {'data': path, 'seed': seed}
    with open("results-R5.txt", "w") as fd:
        fd.write(str(results))
    print(path)
