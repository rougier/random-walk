# Random walk (R1: re-runnable)
# Tested with Python 3
import random

x =  0
walk = []
for i in range(10):
    step = random.choice([-1,+1])
    x += step
    walk.append(x)

print(walk)
