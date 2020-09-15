# Given a directed graph, find the topological ordering of its
# vertices
from collections import deque

# Each vertex will become a source only once and each edge will
# will be accessed and removed once. Therefor time complexity is
# O(V + E), where V is the total number of vertices and E is the
# total number of edges in the graph.

# Space complexity O(V + E), since we are storing all of the edges
# for each vertex in an adjacency list.
def topological_sort(vertices, edges):
    sorted_order = []

    if vertices <= 0:
        return sorted_order

    # a. intialize the graph
    # count of incoming edges
    in_degree = {i: 0 for i in range(vertices)}

    # adjacency list graph
    graph = {i: [] for i in range(vertices)}

    # b. build the graph
    for edge in edges:
        parent, child = edge[0], edge[1]
        # put the child into its parent's list
        graph[parent].append(child)
        # increment the child's in_degree
        in_degree[child] += 1

    # c. find all sources i.e., all vertices with 0 in_degrees
    sources = deque()
    for key, value in in_degree.items():
        if value == 0:
            sources.appendleft(key)

    # d. for each source, add it to the sorted_order and subtract
    # one from its children's in_degree. if a child's in_degree
    # becomes zero, add it to the sources queue
    while sources:
        vertex = sources.pop()
        sorted_order.append(vertex)

        # get the node's children to decreament their in_degrees
        for child in graph.get(vertex):
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.appendleft(child)

    # topological sort is not possible as the graph has a cycle
    if len(sorted_order) != vertices:
        return []

    return sorted_order



def main():
    directed_graph = [[3, 2], [3, 0], [2, 0], [2, 1]]
    print(topological_sort(4, directed_graph))


if __name__ == '__main__':
    main()
