from collections import defaultdict

class Graph: 
    def __init__(self):         
        self.graph = defaultdict(list)
    
    def addEdge(self,u,v):
        self.graph[u].append(v)
 
class BFS:
    def __init__( self, graph):
        self.graph = graph
        self.visited = []
        self.queue = []    
        
    def bfs(self, v):        
        self.queue.append( v )
        self.visited.append( v )
 
        while self.queue: 
            v = self.queue.pop(0)
            print (v, end = " ") 
            
            for u in self.graph[v]:
                if u not in self.visited:
                    self.queue.append( u )
                    self.visited.append( u )
 
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
print( g.graph)

bfs = BFS( g.graph)
bfs.bfs(1)
 
