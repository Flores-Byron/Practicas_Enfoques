import heapq

def ucs(graph, start, goal):
    # Cola de prioridad: (costo acumulado, nodo, camino)
    frontier = [(0, start, [start])]
    visited = set()

    while frontier:
        cost, node, path = heapq.heappop(frontier)

        if node in visited:
            continue
        visited.add(node)

        # Si llegamos al objetivo, devolvemos el camino y el costo
        if node == goal:
            return path, cost

        # Expandir vecinos
        for neighbor, edge_cost in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(frontier, (cost + edge_cost, neighbor, path + [neighbor]))

    return None, float("inf")

# Ejemplo de uso:
# Grafo representado como diccionario: nodo -> [(vecino, costo)]
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [('G', 1)],
    'E': [('G', 2)],
    'F': [('G', 5)],
    'G': []
}

camino, costo = ucs(graph, 'A', 'G')
print("Camino óptimo:", camino)
print("Costo total:", costo)