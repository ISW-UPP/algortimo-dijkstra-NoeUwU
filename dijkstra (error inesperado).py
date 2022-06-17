# -*- coding: utf-8 -*-
import networkx as nx

def dijsktra(Grafo, Nodos):
    
#        Encuentra la geodésica entre un nodo origen y un nodo final en una grafo.
#        
#        Parámetros
#        -----------
#        Grafo : Grafo de Networkx
#            Grafo donde se va a buscar la geodésica.
#        Who : tupla
#            Nodo origen y objetivo, respectivamente.
#        
#        Regresa
#        --------
#        S : lista
#            Camino de nodos de la geodésica
    
    grafo = nx.to_dict_of_lists(Grafo)
    S = []; Queue = []; anterior = [0 for i in range(max(grafo)+1)]; distancia = [0 for i in range(max(grafo)+1)]
    
    for nodo in grafo:
        distancia[nodo] = 10000
        Queue.append(nodo)
        
    distancia[Nodos[0]] = 0
    
    while not len(Queue) == 0:
        distancia_minima = 10000
        for nodo in Queue:
            if distancia[nodo] < distancia_minima:
                distancia_minima = distancia[nodo]
                nodo_temporal = nodo
        nodo_distancia_minima = nodo_temporal
        Queue.remove(nodo_distancia_minima)
        
        for vecino in grafo[nodo_distancia_minima]:
            if distancia[nodo_distancia_minima] == 10000:
                distancia_temporal = 0
            else:
                distancia_temporal = distancia[nodo_distancia_minima]
            distancia_con_peso = distancia_temporal + Grafo[nodo_distancia_minima][vecino]['peso']
            if distancia_con_peso < distancia[vecino]:
                distancia[vecino] = distancia_con_peso
                anterior[vecino] = nodo_distancia_minima
                
        if nodo_distancia_minima == Nodos[1]:
            if anterior[nodo_distancia_minima] != 0 or nodo_distancia_minima == Nodos[0]:
                while nodo_distancia_minima != 0:
                    S.insert(0, nodo_distancia_minima)
                    nodo_distancia_minima = anterior[nodo_distancia_minima]
                return S
                
 
##### Prueba #####               
G = nx.Graph()
aristas = []
#aristas = [(1, 2), (1, 3), (1, 4), (2, 5), (3, 5), (3, 6), (4, 6), (6, 7), (6, 8), (7, 8)]   cantida 10

pesos = []
#pesos = [3, 2, 5, 3, 1, 6, 2, 4, 1, 2]


    



while True:
    print("Menú")
    print("1. Cantidad de aristas")
    print("2. Asignar peso a las aristas")
    print("3. Mostrar Grafo")
    print("4. Dijkstra (Les pedirá el Nodo origen y Nodo destino, calculará en base al peso la ruta mas corta e imprimirá el camino ")

    opcion=input("Opción: ")

    if opcion=="1":
        cantidad=int(input("Ingresar la cantidad de aristas: "))
        print("Ejemplo de como ingresar: 1-2")

        for i in range(cantidad):
            arista_ingresada=input(f"Arista {i+1}: ").split("-")
            aristas.append(   (int(arista_ingresada[0])  ,   int(arista_ingresada[1])   ))



        G.add_edges_from(aristas)

        for i, edge in enumerate(aristas): 
            G[edge[0]][edge[1]]['peso'] = pesos[i]



        print(aristas)


    elif opcion=="2":
        for j in range(cantidad):
            peso=int(input(f"Peso de la arista con vertices {aristas[j][0]} y {aristas[j][1]}: "))
            peso.append(pesos)


    elif opcion=="3":
        for e in range(cantidad):
            print(f"{aristas[e][0]} ------( {peso[e]} )-----> {aristas[e][1]}")


    elif opcion=="4":
        origen=int(input("Nodo de origen: "))
        final=int(input("Nodo de destino: "))

        print(dijsktra(G, (origen, final)))





    print("\n")


