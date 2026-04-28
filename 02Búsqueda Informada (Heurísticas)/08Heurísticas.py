import heapq

def a_estrella(grafo, inicio, objetivo, heuristica):
    #cola de prioridad: (f = g + h, nodo, camino, costo g)
    frontera = [(heuristica[inicio], inicio, [inicio], 0)]
    visitados = set()

    while frontera:
        f, nodo, camino, g = heapq.heappop(frontera)

        if nodo in visitados:
            continue
        visitados.add(nodo)

        #si llegamos al objetivo, devolvemos el camino y el costo
        if nodo ==objetivo:
            return camino, g
        
        #expancion de vecinos
        for vecino, costo in grafo.get(nodo, []):
            if vecino not in visitados:
                g_nuevo = g + costo
                f_nuevo = g_nuevo + heuristica[vecino]
                heapq.heappush(frontera, (f_nuevo, vecino, camino + [vecino], g_nuevo))
    return None, float("inf")

#Ejemplo de uso
#Grafo con costos entre nodos
grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [('G', 1)],
    'E': [('G', 2)],
    'F': [('G', 5)],
    'G': []
}

#Heuristica (estimacion de distancia con el objetivo G)
heuristica = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'E': 0,
    'F': 3,
    'G': 0
}

camino, costo = a_estrella(grafo, 'A', 'G', heuristica)
print("Camino optico con A*:", camino)
print("costo total:", costo)