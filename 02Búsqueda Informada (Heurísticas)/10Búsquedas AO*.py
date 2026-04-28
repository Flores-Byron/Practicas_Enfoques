def ao_estrella(grafo, inicio, heuristica):
    solucion = {}
    frontera = [(heuristica[inicio], inicio)]

    while frontera:
        h, nodo = frontera.pop(0)

        if nodo not in grafo or not grafo[nodo]:
            solucion[nodo] = True
            continue

        mejor_opcion = None
        mejor_costo = float("inf")

        for opcion in grafo[nodo]: # cada opción puede ser AND o OR
            costo = sum(heuristica[sub] for sub in opcion)
            if costo < mejor_costo:
                mejor_costo = costo
                mejor_opcion = opcion


        solucion[nodo] = mejor_opcion
        for sub in mejor_opcion:
            frontera.append((heuristica[sub], sub))

    return solucion

# Ejemplo de grafo AND-OR
grafo_and_or = {
    'A': [['B', 'C'], ['D']],  # A puede resolverse con B y C (AND) o con D (OR)
    'B': [['E']],
    'C': [['F']],
    'D': [['G']],
    'E': [],
    'F': [],
    'G': []
}

heuristica_and_or = {
    'A': 5, 'B': 3, 'C': 2,
    'D': 4, 'E': 0, 'F': 0,
    'G': 0
}

solucion = ao_estrella(grafo_and_or, 'A', heuristica_and_or)
print("Solución encontrada con AO*:", solucion)