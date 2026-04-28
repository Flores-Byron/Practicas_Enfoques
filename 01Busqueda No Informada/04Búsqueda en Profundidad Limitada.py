def dfs_limitada(grafo, inicio, objetivo, limite, visitados = None, camino=None, profundidad=0):
    if visitados is None:
        visitados = set()
    if camino is None:
        camino = []
        
    visitados.add(inicio)
    camino.append(inicio)

    # Si se llega al objetivo, se devuelve el camino
    if inicio == objetivo:
        return camino
    
    # Si se alcanza el límite de profundidad, se regresa None
    if profundidad >= limite:
        return None
    
    #exploramos los vecinos del nodo actual
    for vecino in grafo.get(inicio, []):
        if vecino not in visitados:
            resultado = dfs_limitada(
                grafo, vecino, objetivo, limite,visitados.copy(), camino.copy(), profundidad + 1)
            if resultado:
                return resultado
    return None

# Ejemplo de uso:
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['G'],
    'F': ['G'],
    'G': []
}

camino = dfs_limitada(grafo, 'A', 'G', limite=3)
print("Camino encontrado con límite:", camino)