class Queue:
    def __init__(self):
        self.__data = [] 

    def enqueue(self, value):
        self.__data.append(value)

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow")
            return None
        return self.__data.pop(0)

    def front(self):
        if self.is_empty():
            return None
        return self.__data[0]

    def is_empty(self):
        return len(self.__data) == 0

    def size(self):
        return len(self.__data)


class QueueWrapper:
    def __init__(self):
        self.__queue = Queue() 

    def add(self, value):
        self.__queue.enqueue(value)

    def remove(self):
        return self.__queue.dequeue()

    def peek(self):
        return self.__queue.front()

    def empty(self):
        return self.__queue.is_empty()

    def length(self):
        return self.__queue.size()


q = QueueWrapper()

q.add(10)
q.add(20)
q.add(30)

print("Front:", q.peek())

q.remove()

print("Front after remove:", q.peek())
print("Size:", q.length())