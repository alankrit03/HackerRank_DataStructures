dic = {}
queue = []


def solve(root, x):
    global queue
    # iti is the iterator queue
    # queue is the global queue to keep the record of all the top view elements
    iti = []
    iti.append((root, 0))
    while (len(iti) > 0):
        # print(len(iti))
        x = iti[0][1]
        root = iti[0][0]

        # top view element is the element whose horizontal distance from root is not already present in dic

        if x not in dic:
            queue.append((root.info, x))
            dic[x] = 1
        if root.left != None:
            iti.append((root.left, x - 1))
        if root.right != None:
            iti.append((root.right, x + 1))
        iti.pop(0)


def topView(root):
    solve(root, 0)
    for x in sorted(queue, key=lambda x: x[1]):
        print(x[0], end=" ")

