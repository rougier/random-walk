# Random walk (R2: repeatable)
# Tested with Python 3
import random
from itertools import accumulate

# Random number generator initialization
seed = 1
random.seed(seed)

# Random walk for 10 steps
steps = random.choices([-1,+1], k=10)
x = list(accumulate(steps))

# Display & save results
print(x) 
with open("results-R2-%d.txt" % seed, "w") as file:
    file.write(str(x))
