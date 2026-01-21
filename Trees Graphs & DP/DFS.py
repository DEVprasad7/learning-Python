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
            
            
    def dfs(self, src):
        visited = [False] * self.size
        stack = [src]
        
        while (stack):
            node = stack.pop()
            if visited[node] == False:
                print(node, end=" -> ")
                visited[node] = True
                
            for i in range(self.size):
                if self.mat[node][i] == 1 and visited[i] == False:
                    stack.append(i)
        
        print("End", end="")
        
        
# Example usage:
G = Graph(5, directed=False) # replace it with True if want directed graph (default False)
G.add_edge(0, 1)
G.add_edge(0, 2)
G.add_edge(0, 3)
G.add_edge(1, 3)
G.add_edge(1, 4)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.print()

print()

G.dfs(3)

