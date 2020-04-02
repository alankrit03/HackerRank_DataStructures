def solve(arr, queries):
    n = len(arr)
    ans = []
    for query in queries:
        temp = 0
        k = 0
        for i in range(query):
            if arr[i] > temp:
                temp = arr[i]
                k = i
        m = temp
        s = 1
        e = query
        while e < n:
            if s - 1 == k or arr[e] > temp:
                temp = arr[s]
                k = s
                for i in range(s + 1, e + 1):
                    if arr[i] > temp:
                        temp = arr[i]
                        k = i
                m = min(m, temp)
            s += 1
            e += 1
        ans.append(m)
    return ans
