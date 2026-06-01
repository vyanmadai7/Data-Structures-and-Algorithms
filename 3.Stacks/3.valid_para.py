def is_balanced(s):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}

    for ch in s:
        if ch in mapping.values():
            stack.append(ch)
        else:
            if not stack or stack[-1] != mapping.get(ch):
                return False
            stack.pop()

    return len(stack) == 0


print(is_balanced("()[]{}"))  
print(is_balanced("([)]"))    