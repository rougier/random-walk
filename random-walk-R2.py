# Random walk (R2: repeatable)
# Tested with Python 3
import random

random.seed(1) # RNG initialization

x =  0
walk = []
for i in range(10):
    step = random.choice([-1,+1])
    x += step
    walk.append(x)

print(walk)
# Saving output to disk
with open('results-R2.txt', 'w') as fd:
    fd.write(str(walk))
