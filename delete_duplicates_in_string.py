import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    pre = s[0]#preceeding caracter
    s_out = str(pre)
    Del = 0#number of dletions
    for i in range(1,len(s)):  
        if pre != s[i]:
            s_out +=s [i]
            pre = s[i]
        else: Del += 1
    return Del

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
