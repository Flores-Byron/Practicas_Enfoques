from collections import deque

def reconstruir_camino(padres_inicio, padres_objetivo, punto_encuentro):

    # Reconstruir el camino desde el inicio hasta el punto de encuentro
    camino_inicio = []
    nodo = punto_encuentro
    while nodo is not None:
        camino_inicio.append(nodo)
        nodo = padres_inicio.get(nodo)
    camino_inicio.reverse()

    # Reconstruir el camino desde el objetivo hasta el punto de encuentro
    camino_objetivo = []
    nodo = padres_objetivo.get(punto_encuentro)
    while nodo is not None:
        camino_objetivo.append(nodo)
        nodo = padres_objetivo.get(nodo)
    camino_objetivo.reverse()

    return camino_inicio + camino_objetivo

def busqueda_bidireccional(grafo, inicio, objetivo):
    if inicio == objetivo:
        return [inicio]
    
    #colas para BFS desde el inicio y el objetivo
    cola_inicio = deque([inicio])
    cola_objetivo = deque([objetivo])

    #padres para reconstruir caminos
    padres_inicio = {inicio: None}
    padres_objetivo = {objetivo: None}

    #conjunto de visitados
    visitados_inicio = {inicio}
    visitados_objetivo = {objetivo}

    #creaar expanciones
    while cola_inicio and cola_objetivo:

        #expancion desde el incio
        nodo_actual = cola_inicio.popleft()
        for vecino in grafo.get(nodo_actual, []):
            if vecino not in visitados_inicio:
                padres_inicio[vecino] = nodo_actual
                visitados_inicio.add(vecino)
                cola_inicio.append(vecino)
                if vecino in visitados_objetivo:
                    return reconstruir_camino(padres_inicio, padres_objetivo, vecino)
                
        #expancion desde el objetivo
        nodo_actual = cola_objetivo.popleft()
        for vecino in grafo.get(nodo_actual, []):
            if vecino not in visitados_objetivo:
                padres_objetivo[vecino] = nodo_actual
                visitados_objetivo.add(vecino)
                cola_objetivo.append(vecino)
                if vecino in visitados_inicio:
                    return reconstruir_camino(padres_inicio, padres_objetivo, vecino)
                
    return None

# Ejemplo de uso:
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B', 'G'],
    'E': ['B', 'H'],
    'F': ['C', 'I'],
    'G': ['D', 'I'],
    'H': ['E', 'I'],
    'I': ['F', 'G', 'H']   # Ahora I conecta hacia atrás
}

camino = busqueda_bidireccional(grafo, 'A', 'I')
print("Camino encontrado (bidireccional):", camino)