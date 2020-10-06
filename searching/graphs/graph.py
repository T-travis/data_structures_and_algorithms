from collections import deque


class Graph:
    """Graph is an undirected ajacency-list data structure.
       Each index of the array is an vertex and its list are 
       its adjacent vertices."""

    def __init__(self, file):
        """file represents a txt file with the pattern
            number of vertices
            number of edges
            edge1 edge2
            ...
            ...
           edge1 and edge2 are adjacent (they connect)"""

        with open(f'./graph_data/{file}') as reader:
            self.vertices = int(reader.readline())
            self.edges    = int(reader.readline())
            self._adjacency_list = [deque() for _ in range(self.vertices)]
            for line in reader.readlines():
                edge1, edge2 = int(line[:line.index(' ')]), int(line[line.index(' ')+1:].rstrip())
                self.add_edge(edge1, edge2)

    def add_edge(self, v, w):
        self._adjacency_list[v].appendleft(w)
        self._adjacency_list[w].appendleft(v)

    def adjacents(self, v):
        return self._adjacency_list[v]

    def __str__(self):
        res = ''
        for _list in self._adjacency_list:
            res += (str(_list) + '\n')
        return res


def main():
    graph = Graph('small_graph.txt')
    print(graph)


if __name__ == '__main__':
    main()
