N = int(input())

surplus = start = 0

for i in range(N):
    a, b = input().split()
    surplus += int(a) - int(b)

    if surplus < 0:
        surplus = 0
        start = i + 1

print(start)