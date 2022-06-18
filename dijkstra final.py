from queue import PriorityQueue


class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []

    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight


    def dijkstra(self, start_vertex):
        D = {v:float('inf') for v in range(self.v)}
        D[start_vertex] = 0

        pq = PriorityQueue()
        pq.put((0, start_vertex))

        while not pq.empty():
            (dist, current_vertex) = pq.get()
            self.visited.append(current_vertex)

            for neighbor in range(self.v):
                if self.edges[current_vertex][neighbor] != -1:
                    distance = self.edges[current_vertex][neighbor]
                    if neighbor not in self.visited:
                        old_cost = D[neighbor]
                        new_cost = D[current_vertex] + distance
                        if new_cost < old_cost:
                            pq.put((new_cost, neighbor))
                            D[neighbor] = new_cost
        return D

















while True:
    print("Menú")
    print("1. Cantidad de aristas")
    print("2. Dijkstra (Les pedirá el Nodo origen y Nodo destino, calculará en base al peso la ruta mas corta e imprimirá el camino ")

    opcion=input("Opción: ")

    if opcion=="1":
        cantidad=int(input("Ingresar la cantidad de aristas: "))
        g = Graph(cantidad)
        print("ingresar aristas con formato: vertice_inicial-verticefinal-peso (1-2-1)")

        for i in range(cantidad):
            arista_ingresada=input(f"Arista {i+1}: ").split("-")
            g.add_edge(int(arista_ingresada[0])  ,   int(arista_ingresada[1])  ,   int(arista_ingresada[2]))
            







    elif opcion=="2":
        inicio=int(input("Nodo de origen: "))
        final=int(input("Nodo de destino: "))
        D = g.dijkstra(inicio)

        for vertex in range(len(D)):
            if vertex==final:
                print(f"Distancia del vertice {inicio} al vertice", final, "es", D[vertex])



    print("\n")


