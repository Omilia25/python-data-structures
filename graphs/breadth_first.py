# the depth first traversa of a graph will be done iterratively using a queue

from collections import deque
import queue

# basic starting graph using python library
graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}

def breadth_first_print(graph, start):
    queue = deque([start])
    while len(queue) > 0:
        currentNode = queue[0]
        print(currentNode)
        queue.popleft() 

        # Adding neighbours to the queue
        for neighbour in graph[currentNode]:
            queue.append(neighbour)


breadth_first_print(graph, "a")