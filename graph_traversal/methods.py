from collections import deque  # Import deque from collections for efficient FIFO queue operations


def bfs_list(graph: dict[str, tuple[str]], start_node: str) -> str:
    # Define a function 'bfs_list' that performs BFS on a graph and returns the traversal as a string
    
    not_visited: list[str] = list(graph.keys())  # Initialize a list of all nodes as 'not visited'
    
    if start_node not in not_visited:  # Check if the starting node exists in the graph
        raise ValueError(f"{start_node} is not in this graph")  # Raise an error if the start node isn't in the graph

    bfs: str = ""  # Initialize an empty string to store the BFS traversal order
    queue: deque[str] = deque(start_node)  # Initialize a queue with the start node for BFS traversal

    not_visited.remove(start_node)  # Mark the start node as visited by removing it from 'not_visited'

    while queue:  # Continue the loop as long as there are nodes in the queue
        node = queue.popleft()  # Remove and get the node at the front of the queue
        bfs += f"{node} "  # Append the node to the BFS traversal string

        for i in graph[node]:  # Iterate over all adjacent nodes of the current node
            if i in not_visited:  # Check if the adjacent node has not been visited
                queue.append(i)  # Add the adjacent node to the queue for future processing
                not_visited.remove(i)  # Mark the adjacent node as visited by removing it from 'not_visited'

    return bfs  # Return the BFS traversal order as a string


def dfs_list(graph: dict[str, tuple[str]], start_node: str) -> str:
    # Define a function 'dfs_list' that performs DFS on a graph and returns the traversal as a string
    
    not_visited: list[str] = list(graph.keys())  # Initialize a list of all nodes as 'not visited'
    
    if start_node not in not_visited:  # Check if the starting node exists in the graph
        raise ValueError(f"{start_node} is not in this graph")  # Raise an error if the start node isn't in the graph

    dfs: str = ""  # Initialize an empty string to store the DFS traversal order
    stack: list[str] = list(start_node)  # Initialize a stack with the start node for DFS traversal

    while stack:  # Continue the loop as long as there are nodes in the stack
        node = stack.pop()  # Remove and get the node at the top of the stack
        if node in not_visited:  # Check if the node has not been visited
            dfs += f"{node} "  # Append the node to the DFS traversal string
            not_visited.remove(node)  # Mark the node as visited by removing it from 'not_visited'
            for adjacent_node in reversed(graph[node]):  # Iterate over all adjacent nodes in reverse order
                if adjacent_node in not_visited:  # Check if the adjacent node has not been visited
                    stack.append(adjacent_node)  # Add the adjacent node to the stack for future processing

    return dfs  # Return the DFS traversal order as a string
