from graph import Graph 
from collections import deque


class BreadthFirstPaths:
    """BreadthFirstPaths is a Breadth First Search algorithm implementation."""

    def __init__(self, graph: Graph, start_vertex: int) -> None:
        self.graph = graph
        self.marked = [False] * graph.vertices
        self.edge_to = [0] * graph.vertices
        self.start_vertex = start_vertex
        self.bfs()

    def bfs(self) -> None:
        queue = deque() 
        self.marked[self.start_vertex] = True
        queue.appendleft(self.start_vertex)
        while len(queue) > 0:
            v = queue.pop()
            for w in self.graph.adjacents(v):
                if not self.marked[w]:
                    self.edge_to[w] = v
                    self.marked[w] = True 
                    queue.appendleft(w)

    def has_path_to(self, v: int) -> bool:
        return self.marked[v]

    def path_to(self, v: int) -> list:
        if not self.has_path_to(v): return None 
        path = [] 
        x = v 
        while x != self.start_vertex:
            path.append(x)
            x = self.edge_to[x]
        path.append(self.start_vertex)
        path.reverse()
        return path 



if __name__ == '__main__':
    start = 0
    dfs = BreadthFirstPaths(Graph('tiny_graph_data.txt'), start)
    print(dfs.path_to(0))
    print(dfs.path_to(1))
    print(dfs.path_to(2))
    print(dfs.path_to(3))
    print(dfs.path_to(4))
    print(dfs.path_to(5))
