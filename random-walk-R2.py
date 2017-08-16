# Random walk (R2: repeatable)
# Tested with Python 3
import random

random.seed(0) # RNG initialization

x =  0
path = []
for i in range(10):
    step = random.choice([-1,+1])
    x += step
    path.append(x)

print(path)
# Saving output to disk
with open("results-R2.txt", "w") as fd: 
    fd.write(str(path))
