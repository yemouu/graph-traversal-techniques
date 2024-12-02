import argparse
import datetime
import json
import pathlib
import pprint
import time
from collections import defaultdict

from .graph_helpers import count_edges, generate_binary_tree, generate_graph
from .methods import bfs, dfs_iterative


def main() -> None:
    """Driver script to run through out graph traversal scenarios"""

    parser = argparse.ArgumentParser(prog="graph-traversal")
    parser.add_argument("--run", choices=["demo", "metrics"], help="Run the demo or gather metrics", default="metrics")
    parser.add_argument("--repeat", "-r", type=int, help="How many times to repeat each runtime test", default=5)
    parser.add_argument("--seed", "-s", type=int, help="Integer seed to use for randomized graphs", default=2024)
    parser.add_argument(
        "--nodes",
        "-n",
        type=str,
        help="Space separated list of numbers for the amount of nodes in a graph",
        default="2 4 8 16 32 64 128 256 512 1024 2048 4096 8192 16384 32768 65536 131072",
    )

    args = parser.parse_args()

    if args.run == "demo":
        bintree = generate_binary_tree(8)
        graph = generate_graph(8, 2024)

        print("Binary Tree = ", end="")
        pprint.pprint(bintree)
        print()

        print("Graph = ", end="")
        pprint.pprint(graph)
        print()

        print("BFS Traversal:")
        print("Binary Tree: " + bfs(bintree, 0))
        print("Graph: " + bfs(graph, 0), end="\n\n")

        print("DFS (Iterative) Traversal:")
        print("Binary Tree: " + dfs_iterative(bintree, 0))
        print("Graph: " + dfs_iterative(graph, 0))

        return

    repeat = args.repeat
    graph_seed = args.seed
    graph_sizes = [int(size) for size in args.nodes.split()]

    print(f"{repeat = }\n{graph_seed = }\n{graph_sizes = }")

    bfs_bintree_results: dict[int, list[float]] = defaultdict(list)
    bfs_graph_results: dict[int, list[float]] = defaultdict(list)
    dfs_iterative_bintree_results: dict[int, list[float]] = defaultdict(list)
    dfs_iterative_graph_results: dict[int, list[float]] = defaultdict(list)

    # Print the number of vertices in each graph
    for size in graph_sizes:
        print(f"Size {size}")
        bintree = generate_binary_tree(size)
        graph = generate_graph(size, graph_seed)

        print(f"binary tree: {count_edges(bintree)}")
        print(f"random graph ({graph_seed}): {count_edges(graph)}")
        print()

    # NOTE: This could maybe be parallelized with more processes but i'm
    # unsure how that would effect time.process_time().
    for size in graph_sizes:
        for _ in range(0, repeat):
            bintree = generate_binary_tree(size)
            graph = generate_graph(size, graph_seed)

            start = time.process_time()
            bfs(bintree, 0)
            end = time.process_time()
            bfs_bintree_results[size].append(end - start)

            start = time.process_time()
            bfs(graph, 0)
            end = time.process_time()
            bfs_graph_results[size].append(end - start)

            start = time.process_time()
            dfs_iterative(bintree, 0)
            end = time.process_time()
            dfs_iterative_bintree_results[size].append(end - start)

            start = time.process_time()
            dfs_iterative(graph, 0)
            end = time.process_time()
            dfs_iterative_graph_results[size].append(end - start)

    date = datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S")

    print("Writing results to JSON in current directory...")

    with pathlib.Path(f"./{date}-bfs_bintree.json").open("w") as f:
        f.write(json.dumps(bfs_bintree_results))
    with pathlib.Path(f"./{date}-bfs_graph.json").open("w") as f:
        f.write(json.dumps(bfs_graph_results))
    with pathlib.Path(f"./{date}-dfs_iterative_bintree.json").open("w") as f:
        f.write(json.dumps(dfs_iterative_bintree_results))
    with pathlib.Path(f"./{date}-dfs_iterative_graph.json").open("w") as f:
        f.write(json.dumps(dfs_iterative_graph_results))


if __name__ == "__main__":
    main()
