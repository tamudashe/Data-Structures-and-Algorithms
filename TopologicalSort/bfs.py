from collections import deque


def bfs(graph, vertex):
    # initialize a queue with the starting vertex
    queue = deque([vertex])
    # the level holds distances from the vertex from which we
    # start searching - same as visited hashmap
    level = {vertex: 0}
    parent = {vertex: None}
    # as long as the queue is not empty, we have not visited all
    # vertices
    while queue:
        # pop vertex from the queue
        v = queue.pop()
        for n in graph[v]:
            if n not in level:
                queue.appendleft(n)
                # set the level of n be the level of parent + 1
                level[n] = level[v] + 1
                # record the parent of n
                parent[n] = v
    return level, parent


def main():
    graph = {
            "A": ["B", "C"],
            "B": ["A", "D", "E"],
            "C": ["A", "D"],
            "D": ["B", "C", "E"],
            "E": ["B", "D"]
    }
    level, parent = bfs(graph, "A")
    print("level: ", level)
    print("parent: ", parent)


if __name__ == '__main__':
    main()
