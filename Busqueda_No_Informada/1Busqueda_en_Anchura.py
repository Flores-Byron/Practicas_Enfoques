from collections import deque  # Importamos deque, una estructura tipo cola (FIFO)

def bfs(grafo, inicio):
    visitados = set()  
    # "set" es como una lista, pero no permite repetir elementos.
    # Lo usamos para no visitar el mismo nodo más de una vez.

    cola = deque([inicio])  
    # Creamos la cola y metemos el nodo inicial.
    # Una cola funciona como una fila: el primero en entrar es el primero en salir.

    visitados.add(inicio)  
    # Marcamos el nodo inicial como visitado para no repetirlo.

    while cola:  
        # Este ciclo se ejecuta mientras haya elementos en la cola.

        nodo = cola.popleft()  
        # Sacamos el primer elemento de la cola (FIFO).
        # popleft = quitar el elemento de la izquierda.

        print(nodo, end=" ")  
        # Mostramos el nodo actual.

        for vecino in grafo[nodo]:  
            # Recorremos todos los vecinos (conexiones) del nodo actual.
            # grafo[nodo] devuelve una lista de nodos conectados.

            if vecino not in visitados:  
                # Si ese vecino NO ha sido visitado...

                visitados.add(vecino)  
                # Lo marcamos como visitado (muy importante hacerlo aquí).

                cola.append(vecino)  
                # Lo agregamos a la cola para visitarlo después.

# ---- EJEMPLO DE USO ----

grafo = {
    'A': ['B', 'C'],   # A está conectado con B y C
    'B': ['D', 'E'],   # B con D y E
    'C': ['F'],        # C con F
    'D': [],           # D no tiene conexiones
    'E': ['F'],        # E conecta con F
    'F': []            # F no tiene conexiones
}

# Llamamos a la función empezando desde 'A'
bfs(grafo, 'A')