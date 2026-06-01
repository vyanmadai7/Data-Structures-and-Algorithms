class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_begin(self, data):
        new = Node(data)

        if not self.head:
            self.head = new
            new.next = self.head
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        new.next = self.head
        temp.next = new
        self.head = new

    def insert_end(self, data):
        new = Node(data)

        if not self.head:
            self.head = new
            new.next = self.head
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = new
        new.next = self.head

    def delete(self, key):
        if not self.head:
            return

        if self.head.data == key:
            if self.head.next == self.head:
                self.head = None
                return

            temp = self.head
            while temp.next != self.head:
                temp = temp.next

            temp.next = self.head.next
            self.head = self.head.next
            return

        prev = self.head
        curr = self.head.next

        while curr != self.head:
            if curr.data == key:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next

    def display(self):
        if not self.head:
            print("Empty")
            return

        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next

            if temp == self.head:
                break

        print("(back to head)")


cll = CircularLinkedList()

cll.insert_end(10)
cll.insert_end(20)
cll.insert_end(30)
cll.insert_begin(5)

print("Circular Linked List:")
cll.display()

cll.delete(20)

print("After deleting 20:")
cll.display()