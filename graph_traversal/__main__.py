from .methods import bfs, dfs_iterative


def main():
    """Driver script to run through out graph traversal scenarios"""

    # Initialize some adjacency lists
    adacency_list1: dict[str, tuple[str]] = {
        "A": ("B", "D"),
        "B": ("E",),
        "C": ("D",),
        "D": ("A", "C"),
        "E": ("B",),
    }

    adacency_list2: dict[str, tuple[str]] = {
        "A": ("C",),
        "B": ("C", "D"),
        "C": ("A", "B"),
        "D": ("B",),
        "E": ("D",),
    }

    adacency_list3: dict[str, tuple[str]] = {
        "A": ("B", "C"),
        "B": ("A", "D", "E"),
        "C": ("A", "F", "G"),
        "D": ("B",),
        "E": ("B",),
        "F": ("C",),
        "G": ("C",),
    }

    # Perform Breadth-First Search on adjacency lists starting from node "A"
    print(bfs(adacency_list1, "A"))
    print(bfs(adacency_list2, "A"))
    print(bfs(adacency_list3, "A"))

    # Perform Depth-First Search on our adjacency lists starting at node "A"
    print(dfs_iterative(adacency_list1, "A"))
    print(dfs_iterative(adacency_list2, "A"))
    print(dfs_iterative(adacency_list3, "A"))


if __name__ == "__main__":
    main()
