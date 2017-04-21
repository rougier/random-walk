# Random walk (R2: re-runnable)
# Tested with Python 3
import random
from itertools import accumulate

steps = random.choices([-1,+1], k=10)
x = list(accumulate(steps))
print(x) 
