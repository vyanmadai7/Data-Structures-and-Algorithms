class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_begin(self, data):
        new = Node(data)

        if self.head:
            self.head.prev = new
            new.next = self.head

        self.head = new

    def insert_end(self, data):
        new = Node(data)

        if not self.head:
            self.head = new
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new
        new.prev = temp

    def delete(self, key):
        temp = self.head

        while temp and temp.data != key:
            temp = temp.next

        if not temp:
            return

        if temp.prev:
            temp.prev.next = temp.next
        else:
            self.head = temp.next

        if temp.next:
            temp.next.prev = temp.prev

    def display_forward(self):
        temp = self.head

        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")

    def display_backward(self):
        temp = self.head

        if not temp:
            print("None")
            return

        while temp.next:
            temp = temp.next

        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev

        print("None")


dll = DoublyLinkedList()

dll.insert_end(10)
dll.insert_end(20)
dll.insert_end(30)
dll.insert_begin(5)

print("Forward:")
dll.display_forward()

print("Backward:")
dll.display_backward()

dll.delete(20)

print("After deleting 20:")
dll.display_forward()