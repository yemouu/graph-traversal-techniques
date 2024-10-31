from .methods import bfs_list


def main():
    adacency_list: dict[str, tuple[str]] = {
        "A": ("B", "C"),
        "B": ("A", "D", "E"),
        "C": ("A", "F", "G"),
        "D": ("B",),
        "E": ("B",),
        "F": ("C",),
        "G": ("C",),
    }

    print(bfs_list(adacency_list, "A"))



if __name__ == "__main__":
    main()
