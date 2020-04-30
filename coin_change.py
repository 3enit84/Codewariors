import math
import os
import random
import re
import sys

#
# Complete the 'getWays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c
#

def getWays(n, c):
    from itertools import product
    Lst = []
    Cnum = int(n/min(c))#smallest number of coins needed to meet sum
    for i in range(1,Cnum+1):#number of tries should be as big as the aiming sum
        for s in product(c, repeat=i):#sum all possible combination
            if sum(s) == n:
                if sorted(s) not in Lst:
                    Lst += [sorted(s)]
    #print(Lst)
    return len(Lst)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])#the sum we have to generate
    #print(n)
    m = int(first_multiple_input[1])
    #print(m)
    c = list(map(int, input().rstrip().split()))
    #print(c)
    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)

    fptr.write(str(ways) + '\n')

    fptr.close()
