import sys
 
class Graph():
 
    def __init__(self, vertx):
        self.V = vertx
        self.graph = [[0 for column in range(vertx)]
                      for row in range(vertx)]
 
    def pSol(self, dist):
        print("Distance of vertex from source")
        for node in range(self.V):
            print(node, "t", dist[node])
 

    def minDistance(self, dist, sptSet):
 

        min = sys.maxsize
 

        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
 
        return min_index
 

    def dijk(self, source):
 
        dist = [sys.maxsize] * self.V
        dist[source] = 0
        sptSet = [False] * self.V
 
        for cout in range(self.V):
 
            u = self.minDistance(dist, sptSet)
 
            sptSet[u] = True
 

            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
 
        self.pSol(dist)

f = Graph(4)
f.graph = [[0,20,40,0],
           [0,0,25,30],
           [0,0,0,15],
           [0,0,0,0]]
           
 
f.dijk(0)
