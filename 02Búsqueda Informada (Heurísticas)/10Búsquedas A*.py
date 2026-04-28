import heapq
def a_estrella(grafo, inicio, objetivo, heuristica):
    frontera = [(heuristica[inicio], inicio, [inicio], 0)]
    visitados = set()

    while frontera:
        f, nodo, camino, g = heapq.heappop(frontera)

        if nodo in visitados:
            continue
        visitados.add(nodo)

        if nodo == objetivo:
            return camino, g
        
        for vecino, costo in grafo.get(nodo, []):
            if vecino not in visitados:
                g_nuevo = g + costo
                f_nuevo = g_nuevo + heuristica[vecino]
                heapq.heappush(frontera, (f_nuevo, vecino, camino + [vecino], g_nuevo))
    return None, float("inf")

# Ejemplo de uso A*
grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [('G', 1)],
    'E': [('G', 2)],
    'F': [('G', 5)],
    'G': []
}

heuristica = {
    'A': 7, 'B': 6, 'C': 4,
    'D': 2, 'E': 2, 'F': 3,
    'G': 0
}

camino, costo = a_estrella(grafo, 'A', 'G', heuristica)
print("Camino óptimo con A*:", camino)
print("Costo total:", costo)

