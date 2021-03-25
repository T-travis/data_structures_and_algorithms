

class WeightedUndirectedGraph:

    def __init__(self):
        """Dictionary of keys=vertex, values=dictionary(key=vertex_connected, edge_weight=weight)"""
        self.vertex_list = {}
        self.vertices_count = 0
        self.edges_count = 0

    def add_edge(self, v1, v2, weight=0):
        if v1 not in self.vertex_list:
            self.vertices_count += 1
            self.vertex_list[v1] = {}
        if v2 not in self.vertex_list:
            self.vertices_count += 1
            self.vertex_list[v2] = {}
        self.edges_count += 1
        self.vertex_list[v1][v2] = weight  
        self.vertex_list[v2][v1] = weight 
    
    def get_vertices(self):
        return self.vertex_list.keys()

    def get_edge_weight(self, key1, key2):
        if key1 in self.vertex_list and key2 in self.vertex_list[key1]:
            return self.vertex_list[key1][key2]
        return None

    def get_adjacent_vertices(self, key):
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

    graph = WeightedUndirectedGraph()
    graph.add_edge(0,1,5)
    graph.add_edge(0,5,2)
    graph.add_edge(1,2,4)
    graph.add_edge(2,3,9)
    graph.add_edge(3,4,7)
    graph.add_edge(3,5,3)
    graph.add_edge(4,0,1)
    graph.add_edge(5,4,8)
    graph.add_edge(5,2,1)
    
    key1, key2 = 0, 1
    print(f'weight from {key1} to {key2}: {graph.get_edge_weight(key1, key2)}')
    print()

    # Draw out nodes with connections from this output
    for vertex in graph.get_vertices():
        print('vertex: ' + str(vertex) + ', connected: ' + str(graph.get_adjacent_vertices(vertex)))

    print('vertices: ' + str(graph.get_vertices_count()))
    print('edges: ' + str(graph.get_edges_count()))
    print()

    connected_str = '0 connected to: '
    vertex = graph.get_adjacent_vertices(0)
    for connected in vertex:
        connected_str += (str(connected) + ', ')
    print(connected_str.rstrip(', '))
