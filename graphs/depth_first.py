# The depth first algorithim wil be impemented using a stack
# This wil be acheived iterativey
# And recursively

# basic starting graph using python library
graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}

# depth first print vaues in node takes graph and starting node as 
# arguments

def depth_first_print(graph, start):
    stack = [ start ]
    
    # Curry out the algorithim while stack is not empty
    while len(stack) > 0:
        currentNode = stack[-1]
        print(currentNode)
        stack.pop()

        # add neighbours to stack
        for neighbour in graph[currentNode]:
            stack.append(neighbour)


depth_first_print(graph, "a")


# Depth first implemented recursively
def depth_first_recursive(graph, current):
    print(current) 
    for neighbor in graph[current]:
        depth_first_recursive(graph, neighbor)


depth_first_recursive(graph, "a")