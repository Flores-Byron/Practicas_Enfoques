def dfs(grafo, start, objetivo, visitados=None, camino=None):
    if visitados is None:
        visitados=set()
    if camino is None:
        camino=[]
    visitados.add(start)
    camino.append(start)

    #si se llega al objetivo, se devuelve el camino
    if start == objetivo:
        return camino
    
    #Explorar los vecinos del nodo actual
    for vecino in grafo.get(start, []):
        if vecino not in visitados:
            resultado = dfs(grafo, vecino, objetivo, visitados, camino.copy())
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

camino = dfs(grafo, 'A', 'G')
print("Camino encontrado:", camino)