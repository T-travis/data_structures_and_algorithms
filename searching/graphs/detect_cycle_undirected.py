from undirected_graph import UndirectedGraph
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

    def dfs(self, at, parent):
        self.visited[at] = True
        neighbors = self.graph.get_adjacent_vertices(at)
        # if an unexplored edge has been visited and doesn't equal the parent, we found a cycle
        for neighbor in neighbors:
            if not self.visited[neighbor]:
                if self.dfs(neighbor, at):
                    return True
            elif parent != neighbor:
                return True
        
        return False

    def contains_cycle(self):
        for i in range(self.vertices_count):
            if not self.visited[i]:
                if self.dfs(i, -1):
                    return True

        return False


if __name__ == '__main__':

    # https://www.geeksforgeeks.org/detect-cycle-undirected-graph/
    graph = UndirectedGraph()
    graph.add_edge(1, 0)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(0, 3)
    graph.add_edge(3, 4)
    dfs_graph = DetectCycleDFS(graph)
    if dfs_graph.contains_cycle():
        print('contains cycle!')
    else:
        print('no cycle found')

    graph2 = UndirectedGraph()
    graph2.add_edge(0, 1) 
    graph2.add_edge(1, 2)
    dfs_graph2 = DetectCycleDFS(graph2)
    if dfs_graph2.contains_cycle():
        print('contains cycle!')
    else:
        print('no cycle found')
