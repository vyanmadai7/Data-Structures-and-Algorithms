class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def print_list(head):
    curr = head
    while curr:
        print(curr.data, end="->")
        curr = curr.next
    print("None")


def remove_nth_from_end(head, n):
    dummy = Node(0)
    dummy.next = head

    fast = slow = dummy

    for _ in range(n + 1):
        fast = fast.next

    while fast:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next

    return dummy.next


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print("Original List:")
print_list(head)

head = remove_nth_from_end(head, 2)

print("After removing 2nd node from end:")
print_list(head)