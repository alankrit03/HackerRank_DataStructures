#!/bin/python3

import os
import sys

sys.setrecursionlimit(2048)


def inorder(indexes, i, temp):
    if i == -1:
        return
    if indexes[i - 1][0] == -1 and indexes[i - 1][1] == -1:
        temp.append(i)
        return

    inorder(indexes, indexes[i - 1][0], temp)
    temp.append(i)
    inorder(indexes, indexes[i - 1][1], temp)


def swapNodes(indexes, queries):
    def travel_tree(depth, index):
        if index == -1 or indexes[index - 1] == [-1, -1]:
            return
        if depth % (x) == 0:
            indexes[index - 1][0], indexes[index - 1][1] = indexes[index - 1][1], indexes[index - 1][0]

        travel_tree(depth + 1, indexes[index - 1][0])
        travel_tree(depth + 1, indexes[index - 1][1])

    n = len(queries)
    result = []

    len_ind = len(indexes)

    for x in queries:
        temp = []
        travel_tree(1, 1)
        print(indexes)
        inorder(indexes, 1, temp)
        result.append(temp)

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
