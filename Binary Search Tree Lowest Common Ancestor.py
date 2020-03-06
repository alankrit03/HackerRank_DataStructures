def lca(root, v1, v2):
    #Enter your code here
    if v2<v1:
        v1,v2=v2,v1
    while True:
        if root.info<v1:
            root=root.right
        elif root.info>v2:
            root=root.left
        else:
            return root
