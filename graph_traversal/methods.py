from collections import deque


def bfs_list(graph: dict[str, tuple[str]], start_node: str) -> str:
    not_visited: list[str] = list(graph.keys())
    if start_node not in not_visited:
        raise ValueError(f"{start_node} is not in this graph")

    bfs: str = ""
    queue: deque[str] = deque(start_node)

    not_visited.remove(start_node)

    while queue:
        node = queue.popleft()
        bfs += f"{node} "

        for i in graph[node]:
            if i in not_visited:
                queue.append(i)
                not_visited.remove(i)

    return bfs

def dfs_list(graph: dict[str, tuple[str]], start_node: str) -> str:
    not_visited: list[str] = list(graph.keys())
    if start_node not in not_visited:
        raise ValueError(f"{start_node} is not in this graph")

    dfs: str = ""
    stack: list[str] = list(start_node)

    while stack:
        node = stack.pop()
        if node in not_visited:
            dfs += f"{node} "
            not_visited.remove(node)
            for adjacent_node in reversed(graph[node]):
                if adjacent_node in not_visited:
                    stack.append(adjacent_node)

    return dfs
