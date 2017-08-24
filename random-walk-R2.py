# Random walk (R2: repeatable)
# Tested with Python 3
import random

random.seed(0) # RNG initialization

x =  0
walk = []
for i in range(10):
    if random.uniform(-1, +1) > 0:
        x += 1
    else:
        x -= 1
    walk.append(x)

print(walk)
# Saving output to disk
with open('results-R2.txt', 'w') as fd:
    fd.write(str(walk))
