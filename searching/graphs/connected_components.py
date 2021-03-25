from undirected_graph import UndirectedGraph
from directed_graph import DirectedGraph
from collections import deque


# Time Complexity O(Vertices + Edges)
class ConnectedComponentsDFS:
    """ConnectedComponentsDFS modifies DFS to find connected components.
    
    Comments show code aditions from DFS.
    """

    def __init__(self, graph):
        self.graph = graph
        self.vertices_count = self.graph.get_vertices_count()

        self.visited = [False] * self.vertices_count
        self.previous = [None] * self.vertices_count

        # used to mark vertices that are connected
        # (connected verttices have the same count)
        self.count = 0
        self.connected_components = [0] * self.vertices_count 

    def find_connected_components(self):
        for i in range(self.vertices_count):
            if not self.visited[i]:
                self.count += 1
                self.dfs(i)

    def dfs(self, at):
        self.visited[at] = True
        # marking connecting components of 'at'
        self.connected_components[at] = self.count
        neighbors = self.graph.get_adjacent_vertices(at)
        for neighbor in neighbors:
            if not self.visited[neighbor]:
                self.previous[neighbor] = at
                self.dfs(neighbor)


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
    dfs_graph = ConnectedComponentsDFS(graph)
    dfs_graph.dfs(start)

    dfs_graph.find_connected_components()
    for v, c in enumerate(dfs_graph.connected_components):
        print(f'vertex: {v}, connected number: {c}')
