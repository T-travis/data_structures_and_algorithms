from graph import Graph

class DepthFirstSearch:
    """DepthFirstSearch is a Depth First Search implementation.  This
       algorithm finds all connected vertices from a source."""

    def __init__(self, graph, s):
        self.graph = graph
        self.s = s
        self.count = 0
        self.marked = [False] * self.graph.vertices
        self.dfs(self.graph, s)

    def dfs(self, graph, v):
        self.marked[v] = True
        self.count += 1
        for w in graph.adjacents(v):
            if not self.marked[w]: self.dfs(graph, w)

    def connected_vertices(self):
        connected = []
        for vertice, _ in enumerate(self.marked):
            if self.marked[vertice]: connected.append(vertice)
        return connected



if __name__ == '__main__':
    start = 0
    dfs = DepthFirstSearch(Graph('small_graph.txt'), start)
    print(f'Number of vertices connected to {start}: {dfs.count}')
    print(f"Vertices connected to {start}:")
    print(dfs.connected_vertices())
