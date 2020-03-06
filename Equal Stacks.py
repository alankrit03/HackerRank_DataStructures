import os
import sys


#
# Complete the equalStacks function below.
#
def equalStacks(h1, h2, h3):
    #
    # Write your code here.
    #
    n1, n2, n3 = len(h1), len(h2), len(h3)
    for i in range(n1 - 2, -1, -1):
        h1[i] = h1[i] + h1[i + 1]

    for i in range(n3 - 2, -1, -1):
        h3[i] = h3[i] + h3[i + 1]

    for i in range(n2 - 2, -1, -1):
        h2[i] = h2[i] + h2[i + 1]

    a, b, c = 0, 0, 0
    while (a < n1 and b < n2 and c < n3):
        # print(h1,h2,h3)
        # print('a {},b={}, c={}'.format(a,b,c))
        if h1[a] == h2[b] and h2[b] == h3[c]:
            return h1[a]
        elif h1[a] > h2[b] or h1[a] > h3[c]:
            a += 1
        elif h2[b] > h1[a] or h2[b] > h3[c]:
            b += 1
        elif h3[c] > h1[a] or h3[c] > h2[b]:
            c += 1
    return 0