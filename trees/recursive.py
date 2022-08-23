from turtle import right


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
        return []
    
    left_values = depth_first_values(root.left)
    right_values = depth_first_values(root.right)
    return [root.val] + [left_values] + [right_values]

depth_first_values(a)

# Breadth first values
def breadth_first_values(root):
    if not root:
        return []
breadth_first_values(a)

# sum of tree
def tree_sum(root):
    if not root:
        return 0

    print(root.val + tree_sum(root.left) + tree_sum(root.right))

tree_sum(a)

# search target in root
def tree_includes(root, target):
  
  if root is None:
    return False
  
  if root.val == target:
    return True
  
  return tree_includes(root.left, target) or tree_includes(root.right, target)
 
tree_includes(a, 15)

# Minimum value in a tree
def tree_min_value(root):
  if root is None:
    return float("inf")
  smallest_left_value = tree_min_value(root.left)
  smallest_right_value = tree_min_value(root.right)
  return min(root.val, smallest_left_value, smallest_right_value)

tree_min_value(a)

# max path sum
def max_path_sum(root):
  if root is None:
    return float("-inf")
  
  if root.left is None and root.right is None:
    return root.val
  
  return root.val + max(max_path_sum(root.left), max_path_sum(root.right))

max_path_sum(a)



