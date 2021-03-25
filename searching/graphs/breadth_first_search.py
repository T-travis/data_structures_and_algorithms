from undirected_graph import UndirectedGraph
from directed_graph import DirectedGraph
from collections import deque


# Time Complexity O(Vertices + Edges)
class BFS:

    def __init__(self, graph):
        self.graph = graph
        self.vertices_count = self.graph.get_vertices_count()
        self.visited = [False] * self.vertices_count
        self.previous = [None] * self.vertices_count
        

    def bsf(self, start):
        self.start = start
        queue = deque()  # queue = appendLeft(e), pop()

        # add starting node to queue and mark visited
        queue.appendleft(self.start)
        self.visited[self.start] = True

        while len(queue) > 0:
            node = queue.pop()
            neighbors = self.graph.get_adjacent_vertices(node)

            for neighbor in neighbors:
                if not self.visited[neighbor]:
                    queue.appendleft(neighbor)
                    self.visited[neighbor] = True
                    self.previous[neighbor] = node

    def has_path_to(self, v):
        return self.visited[v]

    def path_to(self, end):

        # check if a path doesn't exist
        if not self.has_path_to(end): return None
        #  reconstruct the path going backwards from end to start
        path = []
        at = end

        while at != self.start:
            path.append(at)
            at = self.previous[at]

        path.append(self.start)
        # reverse so path starts at the start node and ends at the end node
        path.reverse()

        # if start and end are connected, return the path
        return path


if __name__ == '__main__':
    # create graph and add edges for testing bfs
    #graph = UndirectedGraph()
    graph = DirectedGraph()
    graph.add_edge(0,1)
    graph.add_edge(0,5)
    graph.add_edge(1,2)
    graph.add_edge(2,3)
    graph.add_edge(3,4)
    graph.add_edge(3,5)
    graph.add_edge(4,0)
    graph.add_edge(5,4)
    graph.add_edge(5, 2)
    
    bfs_graph = BFS(graph)
    # pass the starting location 
    start = 0
    bfs_graph.bsf(start)

    vertices = bfs_graph.graph.get_vertices()
    for v in vertices:
        print(f"Path from {start} to {v}: {bfs_graph.path_to(v)}")
