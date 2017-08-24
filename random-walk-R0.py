# Random walk (R0: worst you can do)
import random

x = 0
for i in xrange(10):
    if random.uniform(-1, +1) > 0:
        x += 1
    else:
        x -= 1
    print x,
