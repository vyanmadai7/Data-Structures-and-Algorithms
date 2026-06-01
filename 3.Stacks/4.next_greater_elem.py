def next_greater(arr):
    stack = []
    result = [-1] * len(arr)

    for i in range(len(arr)):
        while stack and arr[i] > arr[stack[-1]]:
            idx = stack.pop()
            result[idx] = arr[i]

        stack.append(i)

    return result


print(next_greater([4, 5, 2, 25]))