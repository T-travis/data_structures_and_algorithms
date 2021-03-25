
class Vertex:
    """Vertex represents a node in a graph"""

    def __init__(self, key):
        self.key = key
        self.connected_to = []

    def add_neighbor(self, neighbor):
        self.connected_to.append(neighbor)

    def get_key(self):
        return self.key
    
    def get_connections(self):
        return self.connected_to

    def __str__(self):
        return str(self.key) + ' connected_to: ' + str([x.key for x in self.connected_to])


class UndirectedGraph:

    def __init__(self):
        self.vertex_list = {}
        self.vertex_count = 0

    def _add_vertex(self, key):
        self.vertex_count += 1
        vertex = Vertex(key)
        self.vertex_list[key] = vertex

    def add_edge(self, v1, v2):
        if v1 not in self.vertex_list:
            self._add_vertex(v1)
        if v2 not in self.vertex_list:
            self._add_vertex(v2)
        self.vertex_list[v1].add_neighbor(self.vertex_list[v2])
        self.vertex_list[v2].add_neighbor(self.vertex_list[v1])
    
    def get_vertices(self):
        return self.vertex_list.keys()

    def get_vertex(self, key):
        if key in self.vertex_list:
            return self.vertex_list[key]
        return None

    def __iter__(self):
        return iter(self.vertex_list.values())


if __name__ == "__main__":
    vertex = Vertex(99)
    print(vertex)
    print()

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
    for vertex in graph:
        print(vertex)
        # for w_vertex in vertex.get_connections():
        #     print(f"({vertex.get_key()}, {w_vertex.get_key()})")

    connected_str = '0: '
    vertex = graph.get_vertex(0).get_connections()
    for connected in vertex:
        connected_str += (str(connected.get_key()) + ', ')
    print(connected_str.rstrip(', '))