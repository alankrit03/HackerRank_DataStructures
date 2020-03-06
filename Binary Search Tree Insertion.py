def insert(self, val):
    # Enter you code here.
    if not self.root:
        self.root = Node(val)
    root = self.root
    while 1:
        if root.info > val:
            if root.left:
                root = root.left
            else:
                root.left = Node(val)
                break
        elif root.info < val:
            if root.right:
                root = root.right
            else:
                root.right = Node(val)
                break
        else:
            break

