import datetime
import json
import pathlib
import time
from collections import defaultdict

from .graph_helpers import generate_binary_tree, generate_graph
from .methods import bfs, dfs_iterative


def main() -> None:
    """Driver script to run through out graph traversal scenarios"""

    # TODO: Make these configurable from cli
    repeat = 5
    graph_seed = 2024
    graph_sizes = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072]

    bfs_bintree_results: dict[int, list[float]] = defaultdict(list)
    bfs_graph_results: dict[int, list[float]] = defaultdict(list)
    dfs_iterative_bintree_results: dict[int, list[float]] = defaultdict(list)
    dfs_iterative_graph_results: dict[int, list[float]] = defaultdict(list)

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
