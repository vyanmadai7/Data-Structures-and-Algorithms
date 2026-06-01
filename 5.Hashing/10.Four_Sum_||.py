from collections import defaultdict

def four_sum_count(A,B,C,D):
    count = 0
    hashmap = defaultdict(int)
    for a in A:
        for b in B:
            hashmap[a+b] += 1
    for c in C:
        for d in D:
            count += hashmap.get(-(c+d),0)
    return count

A = [1,2]; B = [-2,-1]; C = [-1, 2]; D = [0, 2]
print(four_sum_count(A,B,C,D))