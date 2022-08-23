class Node:
    def __init__(self, value):
        self.value = value
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


# retun linked list values.
def print_linked_list_Values(root):
    if root is None:
        return 
    print(root.value)
    print_linked_list_Values(root.next)

print_linked_list_Values(a)


# return linked list values sum.
def sum_linked_list_values(head):
    if head is None:
        return 0
    return head.value + sum_linked_list_values(head.next)

sum_linked_list_values(a)

# Find target in a linked list
def find_in_linked_list(head, target):
    if head is None:
        print(False) 
    if head.value == target:
        print(True)
    return find_in_linked_list(head.next, target)


find_in_linked_list(a, 10)



# Get the value of a node at a given index
def get_node_value(head, index):
  if head is None:
    return None
  
  if index == 0:
    return head.val
  
  return get_node_value(head.next, index - 1)

get_node_value(a, 4)

# reverse a linked list
def reverse_linked_list(head, prevNode = None):
    if head is None:
        return prevNode
    nextNode = head.next
    head.next = prevNode
    return reverse_linked_list(nextNode, head)

reverse_linked_list(a)



