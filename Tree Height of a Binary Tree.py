def height(root):
    if not root:
        return -1
    else:
        left_height=height(root.left)
        right_height=height(root.right)
        max_height=max(left_height,right_height)+1
        return max_height