import random 

#definicion del mapa (grafo de regiones y sus vecinos)
mapa = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D"],
    "D": ["B", "C"]
}

#colores disponibles
colores = ["Rojo", "Verde", "Azul"]

#funcion objetivo: minimizar conflictos 8vecinos con el mismo color
def funcion_objetivo(asignacion):
    conflictos = 0
    for region, vecinos in mapa.items():
        for vecino in vecinos:
            if asignacion.get(region) == asignacion.get(vecino):
                conflictos +=1
    return -conflictos #menos conflictos = mejor

#generarvecino: cambiar el color de una region aleatoria
def generar_vecino(asignacion):
    nuevo = asignacion.copy()
    region = random.choice(list(mapa.keys()))
    nuevo[region] = random.choice(colores)
    return nuevo

#busqyeda local para resolver el problema de satisfaccion de restricciones
def resolver_csp(max_iter=1000):
    #asignar inicial aleatoria
    asignacion = {region: random.choice(colores) for region in mapa}
    mejor = asignacion
    mejor_valor = funcion_objetivo(asignacion)

    for _ in range(max_iter):
        vecino = generar_vecino(asignacion)
        valor_vecino = funcion_objetivo(vecino)
        if valor_vecino > mejor_valor:
            mejor, mejor_valor = vecino, valor_vecino
            asignacion = vecino
    
    return mejor, mejor_valor

#ejecucion del algoritmo
solucion, valor = resolver_csp()
print("Asignación encontrada:", solucion)
print("Conflictos:", -valor)