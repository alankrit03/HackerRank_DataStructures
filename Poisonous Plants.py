"""''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Output Format
Output an integer equal to the number of days after which no plants die.

Sample Input
7
6 5 8 4 7 10 9

Sample Output
2
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""


def poisonousPlants(plants):
    stack = []
    maxDays = -10**9

    for plant in plants:
        days = 1

        while stack and stack[-1][0] >= plant:
            _, d = stack.pop()
            days = max(days, d + 1)

        if not stack:
            days = 0

        maxDays = max(maxDays, days)
        stack.append((plant, days))

    return maxDays



if __name__ == '__main__':
    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = poisonousPlants(p)

    print(result)
