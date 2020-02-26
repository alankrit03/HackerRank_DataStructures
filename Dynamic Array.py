#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dynamicArray function below.
def dynamicArray(n, queries):
    lastAnswer=0
    res=[]
    seqlist=[[] for _ in range(n)]
    for query in queries:
        #print(seqlist)
        seq=(query[1]^lastAnswer)%n
        if query[0]==1:
            #print(query)
            seqlist[seq].append((query[-1]))

        else:
            lastAnswer=seqlist[seq][query[-1]%len(seqlist[seq])]
            #print(lastAnswer)
            res.append(lastAnswer)
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nq = input().rstrip().split()

    n = int(nq[0])

    q = int(nq[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
