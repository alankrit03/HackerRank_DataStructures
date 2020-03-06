def levelOrder(root):
    #Write your code here
    queue=[root]
    while queue:
        if queue[0].left:
            queue.append(queue[0].left)
        if queue[0].right:
            queue.append(queue[0].right)
        print(queue.pop(0),end=' ')

