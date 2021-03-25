from directed_graph import DirectedGraph
from collections import deque


# Time Complexity O(Vertices + Edges)
class DetectCycleDFS:
    """DetectCycleDFS modifies DFS to find connected components.

    If an unexplored edge leads to a node visited before, then the graph contains a cycle.
    Comments show code aditions from DFS.
    """

    def __init__(self, graph):
        self.graph = graph
        self.vertices_count = self.graph.get_vertices_count()

        self.visited = [False] * self.vertices_count
        self.on_stack = [False] * self.vertices_count

    def dfs(self, at):
        self.visited[at] = True
        self.on_stack[at] = True
        neighbors = self.graph.get_adjacent_vertices(at)
        for neighbor in neighbors:
            if not self.visited[neighbor]:
                if self.dfs(neighbor):
                    return True
            elif self.on_stack[neighbor]:
                return True
        
        self.on_stack[at] = False
        return False

    def contains_cycle(self):
        for i in range(self.vertices_count):
            if not self.visited[i]:
                if self.dfs(i):
                    return True

        return False



if __name__ == '__main__':

    # https://www.geeksforgeeks.org/detect-cycle-in-a-graph/
    graph1 = DirectedGraph()
    graph1.add_edge(0, 1)
    graph1.add_edge(0, 5)
    graph1.add_edge(0, 6)
    graph1.add_edge(2, 0)
    graph1.add_edge(2, 3)
    graph1.add_edge(3, 5)
    graph1.add_edge(5, 4)
    graph1.add_edge(6, 4)
    graph1.add_edge(6, 9)
    graph1.add_edge(7, 6)
    graph1.add_edge(8, 7)
    graph1.add_edge(9, 10)
    graph1.add_edge(9, 11)
    graph1.add_edge(9, 12)
    graph1.add_edge(11, 12)
    #graph1.add_edge(12, 9)  # makes cycle
    dfs_graph1 = DetectCycleDFS(graph1)
    if dfs_graph1.contains_cycle():
        print('contains cycle!')
    else:
        print('no cycle found')

    graph2 = DirectedGraph() 
    graph2.add_edge(0, 1) 
    graph2.add_edge(0, 2) 
    graph2.add_edge(1, 2) 
    graph2.add_edge(2, 0) 
    graph2.add_edge(2, 3) 
    graph2.add_edge(3, 3)
    dfs_graph2 = DetectCycleDFS(graph2)
    if dfs_graph2.contains_cycle(): 
        print("graph has a cycle")
    else: 
        print("graph has no cycle")
