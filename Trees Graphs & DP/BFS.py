from collections import deque

class Graph:
    def __init__(self, size: int, directed: bool = False):
        self.mat = [ [0]*size for _ in range(size) ]
        self.size = size
        self.directed = directed
        
    def add_edge(self, src: int, dest: int, weight: int = 1):
        if (0 <= src < self.size and 0 <= dest < self.size):
            if self.directed == True:
                self.mat[src][dest] = weight
            else:
                self.mat[src][dest] = weight
                self.mat[dest][src] = weight
                
        else:
            print("Invalid edge Parameter")
            
    def print(self):
        for row in self.mat:
            print(" ".join(map(str, row)))
            
            
    def bfs(self, src):
        visited = [False] * self.size
        queue = deque([src])
        visited[src] = True
        
        while (queue):
            node = queue.popleft()
            print(node, end=" -> ")
                
            for i in range(self.size):
                if (self.mat[node][i] == 1 and visited[i] == False):
                    visited[i] = True
                    queue.append(i)
        print('End', end="")
        
        
# Example usage:
G = Graph(8, directed=False) # replace it with True if want directed graph (default False)
G.add_edge(0, 1)
G.add_edge(0, 3)
G.add_edge(1, 3)
G.add_edge(3, 5)
G.add_edge(3, 4)
G.add_edge(4, 5)
G.add_edge(4, 6)
G.add_edge(6, 2)
G.add_edge(6, 7)
G.print()

print()

G.bfs(0)

