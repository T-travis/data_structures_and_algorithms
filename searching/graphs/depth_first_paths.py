from graph import Graph

class DepthFirstPaths:

    def __init__(self, graph, start_vertex):
        self.start_vertex = start_vertex 
        self.marked = [False] * graph.vertices
        self.edge_to = [0] * graph.vertices
        self.dfs(graph, self.start_vertex)

    def dfs(self, g, v):
        self.marked[v] = True 
        for w in g.adjacents(v):
            if(not self.marked[w]):
                self.edge_to[w] = v
                self.dfs(g, w)

    def has_path_to(self, v):
        return self.marked[v]

    def path_to(self, v):
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
    dfs = DepthFirstPaths(Graph('tiny_graph_data.txt'), start)
    print(dfs.path_to(5))