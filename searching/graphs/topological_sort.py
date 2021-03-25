from collections import deque
from directed_graph import DirectedGraph

# Kahn's Algorithm for solving Topological Sort
# 1. repeatedly remove nodes without any dependencies (nodes without
# any directed edges going to them, degree=0 (degrees=amount of edges
# going to a node)) and add them to the topological ordering
# 2. repead removing nodes without dependencies untill all
# all nodes are processed or a cycle is discovered

# This can be used for Cycle detection in a directed graph

class TopologicalSort:

    def __init__(self, graph):
        self.queue = deque() # appendleft & pop (right)
        self.graph = graph  
        self.vertices = self.graph.get_vertices_count()
        self.in_degree = [0] * self.vertices

    def evaluate_degrees(self):
        for vertex in graph.get_vertices():
            for edge in graph.get_adjacent_vertices(vertex):
                self.in_degree[edge] = self.in_degree[edge] + 1

    def sort(self):
        # evaluate the degree of each node
        self.evaluate_degrees()
        # queue contains the set of nodes with NO incoming edges/degree=0
        for node, degree in enumerate(self.in_degree):
            print(f'degree: {degree},  node: {node}')
            if degree == 0: self.queue.appendleft(node)

        index = 0
        order = [0] * self.vertices

        while len(self.queue) > 0:
            at = self.queue.pop()
            order[index] = at
            index += 1
            for to in self.graph.get_adjacent_vertices(at):
                self.in_degree[to] = self.in_degree[to] - 1
                if self.in_degree[to] == 0:
                    self.queue.appendleft(to)

        if index != self.vertices:
            return None # graph contains a cycle
        return order
        


if __name__ == "__main__":

    graph = DirectedGraph()
    graph.add_edge(0, 1)
    graph.add_edge(0, 5)
    graph.add_edge(0, 6)
    graph.add_edge(2, 0)
    graph.add_edge(2, 3)
    graph.add_edge(3, 5)
    graph.add_edge(5, 4)
    graph.add_edge(6, 4)
    graph.add_edge(6, 9)
    graph.add_edge(7, 6)
    graph.add_edge(8, 7)
    graph.add_edge(9, 10)
    graph.add_edge(9, 11)
    graph.add_edge(9, 12)
    graph.add_edge(11, 12)
    #graph.add_edge(12, 9) # makes cycle
    
    ts = TopologicalSort(graph)
    res = ts.sort()

    if not res: print('The graph conatains a CYCLE')
    else: print(res)
