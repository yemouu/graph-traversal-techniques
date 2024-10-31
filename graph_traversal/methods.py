from collections import deque


def bfs_list(graph: dict[str, tuple[str]], start_node: str) -> str:
    not_visited: list[str] = list(graph.keys())
    if start_node not in not_visited:
        raise ValueError(f"{start_node} is not in this graph")

    bfs: str = ""

    queue: deque[str] = deque()

    queue.append(start_node)
    not_visited.remove(start_node)

    while queue:
        node = queue.popleft()
        bfs += f"{node} "

        for i in graph[node]:
            if i in not_visited:
                queue.append(i)
                not_visited.remove(i)

    return bfs
