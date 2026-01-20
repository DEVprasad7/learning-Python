class Graph:
    def __init__(self, directed=False):
        self.adjList = {}
        self.directed = directed
        
    def add_vertex(self, vertex):
        if vertex not in self.adjList:
            self.adjList[vertex] = []

    def count_vertex(self):
        return len(self.adjList)
    
    def add_edge(self, src, dest):
        self.add_vertex(src)
        self.add_vertex(dest)
        
        if self.directed == True:
            self.adjList[src].append(dest)
        else:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)
            
    def print(self):
        for ver in self.adjList:
            print(ver, " -> ", self.adjList[ver])
            
G = Graph(directed=False)
G.add_edge(0, 1)
G.add_edge(1, 2)
G.add_edge(2, 0)

print(G.count_vertex())

G.print()