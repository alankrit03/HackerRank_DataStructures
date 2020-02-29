def arrayManipulation(n, queries):
    arr = [0] * (n + 1)

    for x in queries:
        arr[x[0]] += x[2]
        if (x[1]) < n:
            arr[x[1] + 1] -= x[2]

    max_val = 0

    update = 0
    for i in range(n + 1):
        update += arr[i]
        max_val = max(max_val, update)

    return max_val


n, k = map(int, input().split())
array = []
for i in range(k):
    array.append([int(x) for x in input().split()])

print(arrayManipulation(n, array))