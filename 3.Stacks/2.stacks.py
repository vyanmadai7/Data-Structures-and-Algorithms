class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


s = Stack()

s.push(10)
s.push(20)
s.push(30)

print("Top element:", s.peek())  
print("Pop:", s.pop())            
print("Pop:", s.pop())            
print("Size:", s.size())          
print("Is empty?", s.is_empty()) 