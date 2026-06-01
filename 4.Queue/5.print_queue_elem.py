def print_queue(qw):
    n = qw.length()
    for _ in range(n):
        x = qw.remove()
        print(x, end=" ")
        qw.add(x)
    print()