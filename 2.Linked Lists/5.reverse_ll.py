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


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

print("Original List:")
print_list(head)

#iterative
def reverse(head):
    prev = None
    curr = head

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    return prev


rev_head_iter = reverse(head)
print("Iteratively Reversed:")
print_list(rev_head_iter)

#recursive
def reverse_recursive(node):
    if not node or not node.next:
        return node

    rest = reverse_recursive(node.next)
    node.next.next = node
    node.next = None

    return rest


rev_head_rec = reverse_recursive(rev_head_iter)

print("Recursively Reversed Back:")
print_list(rev_head_rec)

#Time complexity: O(n)
#Space complexity: O