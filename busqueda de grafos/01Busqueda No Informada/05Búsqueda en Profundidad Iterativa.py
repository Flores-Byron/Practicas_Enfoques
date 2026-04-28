def dfs_iterativa(grafo, inicio, objetivo):

    #Pila: cada elemento es (nodo, camino)
    pila = [(inicio, [inicio])]
    visitados = set()

    while pila:
        nodo, camino = pila.pop()

        if nodo in visitados:
            continue
        visitados.add(nodo)

        # Si se llega al objetivo, se devuelve el camino
        if nodo == objetivo:
            return camino
        
        #se agregaran vecinos a la pila
        for vecino in reversed(grafo.get(nodo, [])):
            if vecino not in visitados:
                pila.append((vecino, camino + [vecino]))
    return None

#Ejemplo de uso:

laberinto = {
    'Entrada': ['A', 'B'],
    'A': ['C'],
    'B': ['D', 'E'],
    'C': ['Salida'],
    'D': ['F'],
    'E': ['F'],
    'F': ['Salida'],
    'Salida': []
}

camino = dfs_iterativa(laberinto, 'Entrada', 'Salida')
print("Camino encontrado en el laberinto:", camino)