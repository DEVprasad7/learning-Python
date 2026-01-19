class Graph:
    def __init__(self, size: int):
        self.mat = [ [0]*size for _ in range(size) ]
        self.size = size
        
    def add_edge(self, src: int, dest: int, weight: int = 1, directed = False):
        if (0 <= src < self.size and 0 <= dest < self.size):
            if directed == True:
                self.mat[src][dest] = weight
            else:
                self.mat[src][dest] = weight
                self.mat[dest][src] = weight
                
        else:
            print("Invalid edge Parameter")
            
    def print(self):
        for row in self.mat:
            print(" ".join(map(str, row)))
        
        
G = Graph(3)
G.add_edge(0, 1)
G.add_edge(0, 2)
G.add_edge(1, 2)
G.print()

