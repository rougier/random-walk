# Random walk (R2: repeatable)
# Tested with Python 3
import random
from itertools import accumulate

# Random number generator initialization
random.seed(1)

# Compute random walk for 10 steps
steps = random.choices([-1,+1], k=10)
x = list(accumulate(steps))
print(x) 
