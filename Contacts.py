root = {'totalWordsBelow':0}
def add(name):
    global root
    curr = root
    for x in name:
        if not curr.get(x):
            curr[x] = {'totalWordsStartWith':0}

        curr = curr[x]
        curr['totalWordsStartWith'] += 1



def find_num_of_contact(prefix):
    curr = root
    for x in prefix:
        if not curr.get(x):
            return 0
        curr = curr[x]
    return curr['totalWordsStartWith']

if __name__ == '__main__':
    queries_rows = int(input())
    queries = []

    for _ in range(queries_rows):
        queries.append(input().split())

    for query in queries:
        if query[0]=='add':
            add(query[1])
        else:
            print(find_num_of_contact(query[1]))

    # print(root)