class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def lca(root, n1, n2):
    if not root:
        return None
    if root.val == n1 or root.val == n2:
        return root

    left = lca(root.left, n1, n2)
    right = lca(root.right, n1, n2)

    if left and right:
        return root
    return left if left else right