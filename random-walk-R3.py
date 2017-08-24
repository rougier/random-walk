# Random walk (R3: reproducible)
# Copyright (c) 2017 Nicolas P. Rougier and Fabien C. Y. Benureau
# Release under the BSD 2-clause license
# Tested with CPython 3.6.2 / macOS 10.12.6 / 64 bits architecture
import sys, subprocess, datetime, random

def generate_walk():
    walk = []
    x = 0
    for i in range(10):
        if random.uniform(-1, +1) > 0:
            x += 1
        else:
            x -= 1
        walk.append(x)
    return walk

# If repository is dirty, don't run anything
if subprocess.call(('git', 'diff-index', '--quiet', 'HEAD')):
    print('Repository is dirty, please commit first')
    sys.exit(1)

# Get git hash if any
revision = subprocess.check_output(('git', 'rev-parse', 'HEAD'))

# Unit test
random.seed(42)
assert generate_walk() == [1, 0, -1, -2, -1, 0, 1, 0, -1, -2]

# Random walk for 10 steps
seed = 1
random.seed(seed)
walk = generate_walk()

# Display & save results
print(walk)
results = {'data'     : walk,
           'seed'     : seed,
           'timestamp': str(datetime.datetime.utcnow()),
           'revision' : revision,
           'system'   : sys.version}
with open('results-R3.txt', 'w') as fd:
    fd.write(str(results))
