#!/bin/python3

import os
import sys


#
# Complete the twoStacks function below.
#


def twoStacks(x, a, b):
    def findInB(s):
        l, h = 0, len(b)

        while h - l > 1:
            m = (l + h) // 2

            if b[m] + s > x:
                h = m
            else:
                l = m
        return l

    #
    # Write your code here.
    #
    for i in range(1, len(a)):
        a[i] = a[i - 1] + a[i]

    for i in range(1, len(b)):
        b[i] = b[i - 1] + b[i]

    ans = 0
    a.insert(0, 0)
    b.insert(0, 0)
    for i in range(len(a)):
        if a[i] <= x:
            ans = max(ans, i + findInB(a[i]))

    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        nmx = input().split()

        n = int(nmx[0])

        m = int(nmx[1])

        x = int(nmx[2])

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = twoStacks(x, a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
