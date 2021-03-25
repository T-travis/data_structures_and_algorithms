from undirected_graph import UndirectedGraph
from directed_graph import DirectedGraph
from collections import deque


# Time Complexity O(Vertices + Edges)
class DFS:

    def __init__(self, graph):
        self.graph = graph
        self.vertices_count = self.graph.get_vertices_count()

        self.visited = [False] * self.vertices_count
        self.previous = [None] * self.vertices_count

    def dfs(self, at):
        self.visited[at] = True
        neighbors = self.graph.get_adjacent_vertices(at)
        for neighbor in neighbors:
            if not self.visited[neighbor]:
                self.previous[neighbor] = at
                self.dfs(neighbor)

    def has_path_to(self, v):
        return self.visited[v]

    def path_to(self, start, end):
        # check if a path doesn't exist
        if not self.has_path_to(end): return None

        #  reconstruct the path going backwards from end to start
        path = []
        at = end

        while at != start:
            path.append(at)
            at = self.previous[at]

        path.append(start)
        # reverse so path starts at the start node and ends at the end node
        path.reverse()

        # if start and end are connected, return the path
        return path

    def contains_cycle(self):
        pass


if __name__ == '__main__':
    # create graph and add edges for testing bfs
    graph = UndirectedGraph()
    #graph = DirectedGraph()
    # graph in Algorithms pg. 529
    graph.add_edge(0, 5)
    graph.add_edge(4, 3)
    graph.add_edge(0, 1)
    graph.add_edge(9, 12)
    graph.add_edge(6, 4)
    graph.add_edge(5, 4)
    graph.add_edge(0, 2)
    graph.add_edge(11, 12)
    graph.add_edge(9, 10)
    graph.add_edge(0, 6)
    graph.add_edge(7, 8)
    graph.add_edge(9, 11)
    graph.add_edge(5, 3)
    
    
    # pass the starting location 
    start = 0
    dfs_graph = DFS(graph)
    dfs_graph.dfs(start)

    vertices = dfs_graph.graph.get_vertices()
    for v in vertices:
        print(f"Path from {start} to {v}: {dfs_graph.path_to(start, v)}")
