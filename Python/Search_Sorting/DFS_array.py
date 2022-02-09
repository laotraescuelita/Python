from collections import defaultdict
 
class Graph:    
    def __init__(self):          
        self.graph = defaultdict(list)
  
    def addEdge(self, u, v):
        self.graph[u].append(v) 
    
class DFS:
    def __init__( self, graph):
        self.visited = []
        self.graph = graph
    
    def dfsVisited(self, v):
        
        self.visited.append(v)
        print(v, end=' ')
          
        for u in self.graph[v]:
            if u not in self.visited:
                self.dfsVisited( u )
  
    def dfs(self, v):
        
        self.dfsVisited(v)
  

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
print( g.graph ) 
  
dfs = DFS( g.graph )
dfs.dfs(1)