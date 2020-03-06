def get_inorder(root, arr):
    if not root:
        return arr
    get_inorder(root.left, arr)
    arr.append(root.data)
    get_inorder(root.right, arr)
    return arr


def check_binary_search_tree_(root):
    arr = get_inorder(root, [])
    if sorted(arr) == arr:
        n = len(arr)
        for i in range(n):
            if arr[i] == arr[i - 1] or arr[i] == arr[(i + 1) % n]:
                return False

        return True

    else:
        return False