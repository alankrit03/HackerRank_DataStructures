
primes, primality = [], [True] * 10001

for i in range(2, 10001):
    if primality[i]:
        primes.append(i)
        primality[2 * i:10001:i] = [False] * (10000 // i - 1)

n, q = map(int, input().split())
A = list(map(int, input().split()))
B, temp = [], []

for p in primes[:q]:
    while A:
        a = A.pop()
        if a % p:
            temp.append(a)
        else:
            B.append(a)

    if B:
        print(*B[::-1], sep="\n")
    A, B, temp = temp[:], [], []

if A:
    print(*A[::-1], sep="\n")

