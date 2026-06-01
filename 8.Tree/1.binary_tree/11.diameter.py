def diameter(root):
    res = 0

    def height(node):
        nonlocal res
        if not node:
            return 0

        left = height(node.left)
        right = height(node.right)

        res = max(res, left + right)

        return 1 + max(left, right)

    height(root)
    return res