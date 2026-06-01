def reverse_k(qw, k):
    stack = []

    for _ in range(k):
        stack.append(qw.remove())

    while stack:
        qw.add(stack.pop())

    for _ in range(qw.length() - k):
        qw.add(qw.remove())