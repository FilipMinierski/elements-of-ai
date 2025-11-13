
import math
import random
import numpy as np
import io
from io import StringIO
import numpy as np
import random

def generate(p1):
    # change this so that it generates 10000 random zeros and ones
    # where the probability of one is p1
    seq = np.empty(10000)
    for i in range(10000):
        if random.random() < p1:
            seq[i] = 1
        else:
            seq[i] = 0

    return seq

def count(seq):
    # insert code to return the number of occurrences of 11111 in the sequence
    n = 0
    counter = 0

    for num in seq:
        if num == 1:
            counter += 1
        else:
            counter = 0
        
        if counter >= 5:
            n += 1
            
    return n

def main(p1):
    seq = generate(p1)
    return count(seq)

print(main(2/3))

  
