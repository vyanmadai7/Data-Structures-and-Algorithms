def is_palindrome(qw):
    temp = []
    n = qw.length()

    for _ in range(n):
        x = qw.remove()
        temp.append(x)
        qw.add(x)

    return temp == temp[::-1]