import random

#definir el mapa (grafo de regiones y sus vecinos)
mapa = {
    "1": ["2", "3"],
    "2": ["1", "3", "4"],
    "3": ["1", "2", "4"],
    "4": ["2", "3"]
}


# Colores disponibles
colores = ["Naranja", "Amarillo", "Morado"]

#contar conflictos en una asignacion
def contar_conflictos(asignacion):
    conflictos = 0
    for region, vecinos in mapa.items():
        for vecino in vecinos:
            if asignacion[region] == asignacion[vecino]:
                conflictos += 1
    return conflictos

#algoritmo de minimos conflictos
def min_conflictos(max_iter=1000):

    #asignacion inicial aleatoria
    asignacion = {region: random.choice(colores) for region in mapa}

    for _ in range(max_iter):

        #si no hay conflictos, devolver solucion
        if contar_conflictos(asignacion) == 0:
            return asignacion
        
        #elegir una region en conflicto
        regiones_conflictivas = [r for r in mapa if any(asignacion[r] == asignacion[v] for v in mapa[r])]
        region = random.choice(regiones_conflictivas)

        #elegir color que minimice conflictos
        mejor_color = min(colores, key=lambda c: contar_conflictos({**asignacion, region: c}))
        asignacion[region] = mejor_color

    return None #si es que no se encontro solucion

#ejecucion
solucion = min_conflictos()

#mostrar el resultado
if solucion:
    print("Solución encontrada con Mínimos-Conflictos:")
    for region, color in solucion.items():
        print(f"Región {region} → {color}")
else:
    print("No se encontró solución válida.")