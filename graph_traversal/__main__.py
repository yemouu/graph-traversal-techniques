from .methods import bfs_list, dfs_list  # Import bfs_list and dfs_list functions from the methods module


def main():
    # Define the main function where the graph adjacency lists and traversal outputs are handled

    adacency_list1: dict[str, tuple[str]] = {
        "A": ("B", "D"),
        "B": ("E",),
        "C": ("D",),
        "D": ("A", "C"),
        "E": ("B",),
    }
    # Initialize 'adjacency_list1' as a dictionary representing a graph with nodes and their adjacent nodes

    adacency_list2: dict[str, tuple[str]] = {
        "A": ("C",),
        "B": ("C", "D"),
        "C": ("A", "B"),
        "D": ("B",),
        "E": ("D",),
    }
    # Initialize 'adjacency_list2' as another dictionary representing a different graph structure

    adacency_list3: dict[str, tuple[str]] = {
        "A": ("B", "C"),
        "B": ("A", "D", "E"),
        "C": ("A", "F", "G"),
        "D": ("B",),
        "E": ("B",),
        "F": ("C",),
        "G": ("C",),
    }
    # Initialize 'adjacency_list3' as a third dictionary representing a different graph structure

    print(bfs_list(adacency_list1, "A"))  # Perform BFS on 'adjacency_list1' starting from node "A" and print the result
    print(bfs_list(adacency_list2, "A"))  # Perform BFS on 'adjacency_list2' starting from node "A" and print the result
    print(bfs_list(adacency_list3, "A"))  # Perform BFS on 'adjacency_list3' starting from node "A" and print the result

    print(dfs_list(adacency_list1, "A"))  # Perform DFS on 'adjacency_list1' starting from node "A" and print the result
    print(dfs_list(adacency_list2, "A"))  # Perform DFS on 'adjacency_list2' starting from node "A" and print the result
    print(dfs_list(adacency_list3, "A"))  # Perform DFS on 'adjacency_list3' starting from node "A" and print the result


if __name__ == "__main__":  # Check if the script is being run directly (not imported as a module)
    main()  # Call the main function to execute the code
