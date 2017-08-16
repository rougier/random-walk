# Random walk (R1: re-runnable)
# Tested with Python 3
import random

walk, total = [], 0
for i in range(10):
    step = random.choice([-1,+1])
    total += step
    walk.append(total)

print(walk)
