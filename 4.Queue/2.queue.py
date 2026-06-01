class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue Underflow")
            return
        return self.queue.pop(0)

    def front(self):
        if len(self.queue) == 0:
            return None
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0


q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print("Front:", q.front())

q.dequeue()

print("Front after dequeue:", q.front())