import random
from collections import deque
from functools import cache


@cache
def generate_binary_tree(number_of_nodes: int) -> dict[int, tuple[int | None]]:
    """Generate a binary tree

    Args:
        number_of_nodes: Integer representing the number of nodes in
          the graph. Must be larger than 0.

    Returns:
        Adjacency list represented by a dictionary with integers as its
        keys and a tuple of integers as their value. The adjacency list
        represents a bi-directional graph.

    Raises:
        ValueError: the number_of_nodes is less than 1
    """

    # Raise an error if the number_of_nodes is a negative number
    if number_of_nodes < 1:
        raise ValueError("number_of_nodes is less than 1")

    # Initialize both the graph and a queue with node 0. The queue here
    # is being used to ensure that all nodes are being populated. We
    # want each node to have two children which is why we add each node
    # to the queue twice.
    graph: dict[int, tuple[int | None]] = {0: ()}
    queue: deque[int] = deque([0, 0])

    # For each node, pop an existing node off of the queue
    # (this is now the parent node), and add our new node to its
    # adjacency list. Then we add the parent node to the new node's
    # adjacency list and add the new node to the queue
    for node in range(1, number_of_nodes):
        parent_node = queue.popleft()
        graph[parent_node] = graph[parent_node] + (node,)

        graph[node] = (parent_node,)
        queue.extend([node, node])

    # Return the graph we built
    return graph


@cache
def generate_graph(number_of_nodes: int, seed: int) -> dict[int, tuple[int | None]]:
    """Generate a random graph

    By supplying a seed, the same graph can be generated each time.

    Args:
        number_of_nodes: Integer representing the number of nodes in
          the graph. Must be larger than 0.
        seed: An integer used to seed the random number generator.
          Using this, the same graph can be reliably generated. If
          None, the graph will be random.
    """
    # Raise an error if the number_of_nodes is a negative number
    if number_of_nodes < 1:
        raise ValueError("number_of_nodes is less than 1")

    # Initialize random number generator with a seed
    rng = random.Random(seed)

    # Initialize a graph with node 0.
    graph: dict[int, tuple[int | None]] = {0: ()}

    # For each node, randomly select a parent and make a connection
    # between them
    for node in range(1, number_of_nodes):
        parent_node = rng.randint(0, node - 1)
        graph[parent_node] = graph[parent_node] + (node,)

        graph[node] = (parent_node,)

    # Return the graph we built
    return graph
