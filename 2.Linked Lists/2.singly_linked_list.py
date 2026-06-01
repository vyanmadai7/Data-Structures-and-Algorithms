class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        new = Node(data)

        if not self.head:
            self.head = new
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new

    def insert_begin(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new

    def delete(self, key):
        temp = self.head

        if temp and temp.data == key:
            self.head = temp.next
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if not temp:
            return

        prev.next = temp.next

    def display(self):
        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


ll = SinglyLinkedList()

ll.insert_end(10)
ll.insert_end(20)
ll.insert_end(30)

ll.insert_begin(5)

print("Linked List:")
ll.display()

ll.delete(20)

print("After deleting 20:")
ll.display()