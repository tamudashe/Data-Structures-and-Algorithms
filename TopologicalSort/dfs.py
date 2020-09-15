def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            for v in graph[vertex]:
                stack.append(v)

    return visited


def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next_node in graph[start]:
        if next_node not in visited:
            dfs_recursive(graph, next_node, visited)
    return visited


def main():
    # graph representation using an adjacency list
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D"],
        "C": ["A", "E", "F"],
        "D": ["B", "G"],
        "E": ["C", "G"],
        "F": ["C"],
        "G": ["D", "E", "H"],
        "H": ["G"]
    }
    print("iterative: ", dfs_iterative(graph, "A"))
    print("recursive: ", dfs_recursive(graph, "A"))

if __name__ == '__main__':
    main()
