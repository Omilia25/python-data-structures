from collections import deque
import queue


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


a = Node(10)
b = Node(20)
c = Node(30)
d = Node(40)
e = Node(50)
f = Node(60)
g = Node(70)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g

# depth first traversal
def depth_first_values(root):
    if not root:
        return[]

    stack = [root]
    values = []

    while stack:
        currentNode = stack.pop()
        values.append(currentNode.val)
        if currentNode.right:
            stack.append(currentNode.right)
        if currentNode.left:
            stack.append(currentNode.left)
    print(values)

depth_first_values(a)


# breadth first traversal
def breadth_first_traversal(root):
    if not root:
        return []
    
    queue = deque([root])
    values = []

    while queue:
        currentNode = queue.popleft()
        values.append(currentNode.val)

        if currentNode.left:
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)
    
    print(values)

breadth_first_traversal(a)

# sum of tree node values
def tree_sum(root):
    if not root:
        return 0
    
    stack = [root]
    sum = 0
    while stack:
        currentNode = stack.pop()
        sum += currentNode.val

        if currentNode.right:
            stack.append(currentNode.right)
        if currentNode.left:
            stack.append(currentNode.left)
    print(sum)

tree_sum(a)

# Search for a target
def tree_includes(root, target):
  if not root:
    return False
  
  queue = deque([root])
  while queue:
    currentNode = queue.popleft()
    if currentNode.val == target:
      return True
    
    if currentNode.left:
      queue.append(currentNode.left)
    if currentNode.right:
      queue.append(currentNode.right)
      
  return False
  
tree_includes(a, 15)

# find the minimum value in the tree
def tree_min_value(root):
  if not root:
    return 
  
  stack = [root]
  min = float("inf")
  
  while stack:
    currentNode = stack.pop()
    if currentNode.val < min:
      min = currentNode.val
    
    if currentNode.right:
      stack.append(currentNode.right)
    if currentNode.left:
      stack.append(currentNode.left)
      
  print(min)
  
tree_min_value(a)
    
    