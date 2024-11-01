from .methods import bfs_list, dfs_list


def main():
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

    print(bfs_list(adacency_list1, "A"))
    print(bfs_list(adacency_list2, "A"))
    print(bfs_list(adacency_list3, "A"))

    print(dfs_list(adacency_list1, "A"))
    print(dfs_list(adacency_list2, "A"))
    print(dfs_list(adacency_list3, "A"))


if __name__ == "__main__":
    main()
