

class UndirectedGraph:

    def __init__(self):
        """vertex_list is a dictionary with keys=vertex, values=[connected_vertices]"""
        self.vertex_list = {}
        self.vertices_count = 0
        self.edges_count = 0

    def add_edge(self, v1, v2):
        """Add an edge to the graph"""
        if v1 not in self.vertex_list:
            self.vertices_count += 1
            self.vertex_list[v1] = []
        if v2 not in self.vertex_list:
            self.vertices_count += 1
            self.vertex_list[v2] = []
        self.edges_count += 1
        self.vertex_list[v1].append(v2)
        self.vertex_list[v2].append(v1)
    
    def get_vertices(self):
        """Get all vertices of the graph"""
        return self.vertex_list.keys()

    def get_adjacent_vertices(self, key):
        """Get all connected vertices to a given vertex"""
        if key in self.vertex_list:
            return self.vertex_list[key]
        return None

    def get_vertices_count(self):
        return self.vertices_count

    def get_edges_count(self):
        return self.edges_count

    def __iter__(self):
        return iter(self.vertex_list.values())


if __name__ == "__main__":

    graph = UndirectedGraph()
    graph.add_edge(0,1)
    graph.add_edge(0,5)
    graph.add_edge(1,2)
    graph.add_edge(2,3)
    graph.add_edge(3,4)
    graph.add_edge(3,5)
    graph.add_edge(4,0)
    graph.add_edge(5,4)
    graph.add_edge(5,2)
    
    # Draw out nodes with connections from this output
    for vertex in graph.get_vertices():
        print(str(vertex) + ' connected_to: ' + str(graph.get_adjacent_vertices(vertex)))

    print('vertices: ' + str(graph.get_vertices_count()))
    print('edges: ' + str(graph.get_edges_count()))

    connected_str = '0: '
    vertex = graph.get_adjacent_vertices(0)
    for connected in vertex:
        connected_str += (str(connected) + ', ')
    print(connected_str.rstrip(', '))