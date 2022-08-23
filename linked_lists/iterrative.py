from itertools import count


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


a = Node(10)
b = Node(20)
c = Node(30)
d = Node(40)
e = Node(50)
f = Node(60)
g = Node(70)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g

# Traversing a linked list
def linked_list_values(head):
    currentNode = head
    while currentNode is not None:
        print(currentNode.val)
        currentNode = currentNode.next

linked_list_values(a)

# Find the sum of linked list elements
def sum_linked_list(head):
    currentNode = head
    sum = 0
    while currentNode is not None:
        sum += currentNode.val
        currentNode = currentNode.next
    print(sum)

sum_linked_list(a)

# Find in a list.
def find_in_list(head, target):
    currentNode = head
    while currentNode is not None:
        if currentNode.val == target:
            print(True)
        currentNode = currentNode.next
    print(False) 

find_in_list(a, 97)

# return value of element in a given index
def index_linked_in_value(head, index):
    count = 0
    currentNode = head
    while head is not None:
        if count == index:
            return currentNode.val
        
        currentNode = currentNode.next
        count += 1

    return None
index_linked_in_value(a, 3)

# Reverse linked list order
def reverse_linked_list(head):
    prevNode = None
    currentNode = head
    while currentNode is not None:
        nextNode = currentNode.next
        currentNode.next = prevNode
        prevNode = currentNode
        currentNode = nextNode
    return prevNode

reverse_linked_list(a)

# Zipper listc


        
        
        