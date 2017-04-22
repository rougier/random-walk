# Random walk (R5: re-usable)
# Copyright (c) 2017 Nicolas P. Rougier and Fabien C.Y. Benureau
# Release under the BSD 2-clause license
# Tested with Python 3.6 / Numpy 1.12.0 / macOS 10.12.4 / 64 bits architecture
import random
import numpy as np

def walk(rng, n):
    """ Random walk for n steps """

    steps = 2*(rng.uniform(-1,+1,n) > 0) - 1
    return steps.cumsum().tolist()

def rng(seed):
    """ Return a random number generator initialized with seed """ 
    
    rng = random.Random()
    rng.seed(seed)
    _, keys, _ = rng.getstate()
    rng = np.random.RandomState()
    state = rng.get_state()
    rng.set_state((state[0], keys[:-1], state[2], state[3], state[4]))
    return rng

def test():
    """ Unit tests """

    return  walk(rng(seed=1), 10) == [-1, 0, 1, 0, -1, -2, -1, 0, -1, -2]
    
    
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser("Random walk")
    parser.add_argument('--seed', type=int, default=1,
                        help='Seed for random number generator ')
    parser.add_argument('n', type=int, default=10,
                        help='Number of step(s) to walk')
    args = parser.parse_args()

    # Random walk for n steps
    x = walk(rng(args.seed), args.n)

    # Display & save results
    print("Seed:", args.seed)
    print("Number of steps:", args.n)
    print("Result:",  x)
    with open("results-R5-%d.txt" % args.seed, "w") as file:
        file.write(str(x))
