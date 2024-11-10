# Import deque for efficient FIFO operations
from collections import deque


def bfs(graph: dict[int, tuple[int]], start_node: int) -> str:
    """Perform Breadth-First Search on a graph

    Args:
        graph: Adjacency list in the form of a dictionary that takes an
          integer as its key (this is the node) and a tuple of integers
          (nodes) as its value.
        start_node: An integer representing a node inside the graph.

    Returns:
        A string representing the order that nodes were visted.

    Raises:
        ValueError: The start_node was not inside the graph.
    """

    # Mark all nodes as 'not visited'
    not_visited: list[int] = list(graph.keys())

    # Check if the starting node exists in the graph and raise an error
    # if it does not
    if start_node not in not_visited:
        raise ValueError(f"{start_node} is not in this graph")

    # Initialize an empty string to store the BFS traversal order
    result: str = ""

    # Initialize a queue with the start node and mark it as visited
    queue: deque[int] = deque([start_node])
    not_visited.remove(start_node)

    # While the queue has nodes, remove the oldest item from the queue,
    # visit/process it, and then add its adjacent nodes to the queue
    # and mark them as visited.
    while queue:
        node = queue.popleft()
        result += f"{node} "

        for i in graph[node]:
            if i in not_visited:
                queue.append(i)
                not_visited.remove(i)

    # Return the traversal order
    return result


def dfs_iterative(graph: dict[int, tuple[int]], start_node: int) -> str:
    """Perform Depth-First Search on a graph using iteration

    Args:
        graph: Adjacency list in the form of a dictionary that takes an
          integer as its key (this is the node) and a tuple of integers
          (nodes) as its value.
        start_node: An integer representing a node inside the graph.

    Returns:
        A string representing the order that nodes were visted.

    Raises:
        ValueError: The start_node was not inside the graph.
    """

    # Mark all nodes as 'not visited'
    not_visited: list[int] = list(graph.keys())

    # Check if the starting node exists in the graph and raise an error
    # if it does not
    if start_node not in not_visited:
        raise ValueError(f"{start_node} is not in this graph")

    # Initialize an empty string to store the DFS traversal order
    result: str = ""

    # Initialize a stack with the start node for DFS traversal
    stack: list[int] = [start_node]

    # While the stack has nodes, pop the youngest item from the stack.
    # If the node has not been visited before, visit/process it and
    # mark it as visited. Then for each adjacent, if it has not been
    # visited, add it to the stack
    while stack:
        node = stack.pop()

        if node in not_visited:
            result += f"{node} "
            not_visited.remove(node)

            # We do this in reversed order otherwise we get a result
            # that would be different from a recursive implementation.
            for adjacent_node in reversed(graph[node]):
                if adjacent_node in not_visited:
                    stack.append(adjacent_node)

    # Return the traversal order
    return result
