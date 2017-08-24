# Random walk (R1: re-runnable)
# Tested with Python 3
import random

x =  0
walk = []
for i in range(10):
    if random.uniform(-1, +1) > 0:
        x += 1
    else:
        x -= 1
    walk.append(x)

print(walk)
