from .graph_helpers import generate_binary_tree
from .methods import bfs, dfs_iterative


def main() -> None:
    """Driver script to run through out graph traversal scenarios"""

    # Perform Breadth-First Search
    print(bfs(generate_binary_tree(10), 0))
    print(bfs(generate_binary_tree(100), 0))
    print(bfs(generate_binary_tree(1000), 0))

    # Perform Depth-First Search
    print(dfs_iterative(generate_binary_tree(10), 0))
    print(dfs_iterative(generate_binary_tree(100), 0))
    print(dfs_iterative(generate_binary_tree(1000), 0))


if __name__ == "__main__":
    main()
