class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def print_list(head):
    while head:
        print(head.data, end="->")
        head = head.next
    print("None")


def merge_sorted_lists(l1, l2):
    dummy = Node(0)
    tail = dummy

    while l1 and l2:
        if l1.data <= l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next

        tail = tail.next

    if l1:
        tail.next = l1
    else:
        tail.next = l2

    return dummy.next


l1 = Node(1)
l1.next = Node(3)
l1.next.next = Node(5)

l2 = Node(2)
l2.next = Node(4)
l2.next.next = Node(6)

merged = merge_sorted_lists(l1, l2)

print("Merged List:")
print_list(merged)