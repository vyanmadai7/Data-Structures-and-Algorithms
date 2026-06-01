def is_identical(a, b):
    if not a and not b:
        return True
    if not a or not b:
        return False

    return (a.val == b.val and
            is_identical(a.left, b.left) and
            is_identical(a.right, b.right))