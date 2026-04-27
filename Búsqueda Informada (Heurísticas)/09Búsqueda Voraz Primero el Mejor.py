import heapq

def voraz_primero_el_mejor(grafo, inicio, objetivo, heuristica):
    #cola de prioridad: (h(n), nodo, camino)
    frontera = [(heuristica[inicio], inicio, [inicio])]
    visitados = set()

    while frontera:
        h, nodo, camino = heapq.heappop(frontera)

        if nodo in visitados:
            continue
        visitados.add(nodo)

        #si llegamos al objetivo, devolvemos el camino
        if nodo == objetivo:
            return camino
        
        #expancion de vecinos
        for vecino, costo in grafo.get(nodo, []):
            if vecino not in visitados:
                heapq.heappush(frontera, (heuristica[vecino], vecino, camino + [vecino]))
    return None

#Ejemplo de uso
grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [('G', 1)],
    'E': [('G', 2)],
    'F': [('G', 5)],
    'G': []
}

# Heurística: estimación de distancia al objetivo G
heuristica = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 2,
    'E': 2,
    'F': 3,
    'G': 0
}

camino = voraz_primero_el_mejor(grafo, 'A', 'G', heuristica)
print("Camino encontrado (Voraz Primero el Mejor):", camino)