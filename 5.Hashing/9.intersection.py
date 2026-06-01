def intersection(num1,num2):
    set1 = set(num1)
    set2 = set(num2)
    return list(set1 & set2)

print(intersection([1,2,2,1],[2,2]))