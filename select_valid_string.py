import math
import os
import random
import re
import sys

# Complete the isValid function below.
def isValid(s):
    Lst = []
    for i in s:
        Lst += [i]
    print(Lst)
    from collections import Counter
    Dic = dict(Counter(Lst))
    print(Dic)
    DupLst = []#list of duplicate counts
    for i in range(len(list(Dic.items()))):
        DupLst += [list(Dic.items())[i][1]]
    DupCntLst = []#list of duplicated values
    DupMemLst = []#list of duplicated members
    DupCnt = dict(Counter(DupLst))
    print(DupCnt)
    for i in range(len(list(DupCnt.items()))):
        DupCntLst += [list(DupCnt.items())[i][1]]
        DupMemLst += [list(DupCnt.items())[i][0]]
    print('DupLst',DupLst)
    print('DupCntLst',DupCntLst)
    if len(DupCntLst)==1:#all characters happened the same amount of times
        return 'YES'
    if len(DupCntLst)==2:
        if DupLst.count(1) == 1:#the single 1 in DupLst
            if 1 in DupCntLst:#there is a single value that can be removed etirely
                return 'YES'
            else: return 'NO'
        elif 1 in DupCntLst:#single case of duplicated value
            DupMemLst.sort()
            print('MemLst',DupMemLst)
            if DupMemLst[1]-DupMemLst[0] == 1:#only one duplicated value can be removed
                return 'YES'
            else: return 'NO'
        else: return 'NO'
    else: return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    #s = 'aaaaabc'
    result = isValid(s)
    print(result)
    fptr.write(result + '\n')

    fptr.close()
