from collections import deque

def busqueda_en_grafos(grafo, inicio, objetivo):
    # Cola para búsqueda en anchura
    cola = deque([(inicio, [inicio])])
    visitados = set([inicio])

    while cola:
        nodo, camino = cola.popleft()

        # Si llegamos al objetivo, devolvemos el camino
        if nodo == objetivo:
            return camino

        # Explorar vecinos
        for vecino in grafo.get(nodo, []):
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append((vecino, camino + [vecino]))

    return None

# Ejemplo de uso:
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['H'],
    'F': ['I'],
    'G': [],
    'H': ['I'],
    'I': []
}

camino = busqueda_en_grafos(grafo, 'A', 'I')
print("Camino encontrado (búsqueda en grafos):", camino)