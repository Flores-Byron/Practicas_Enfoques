import random

#funcion objetivo: maximizar -(x-5)^2 + 25 (maximo en x=5)
def funcion_objetivo(x):
    return -(x-5)**2 + 25

#crear un individuo aleatorio
def crear_individuo():
    return random.randint(0, 10)

#crear poblacion inicial
def crear_poblacion(tamaño):
    return [crear_individuo() for h in range(tamaño)]

#seleccionar los mejores individuos
def seleccion(poblacion):
    return sorted(poblacion, key=funcion_objetivo, reverse=True)[:2]

#cruzar dos individuos
def cruce(ind1, ind2):
    return (ind1 + ind2) // 2

#alterar ligeramente un idividuo
def mutacion(individuo):
    return individuo + random.choice([-1, 1])

#algoritmo genetico
def algoritmo_genetico(tamaño_poblacion=6, generaciones=20):
    poblacion = crear_poblacion(tamaño_poblacion)

    for _ in range(generaciones):
        #selccionar padres
        padres = seleccion(poblacion)

        #nueva generacion
        nueva_poblacion = padres[:]
        while len(nueva_poblacion) < tamaño_poblacion:
            hijo = cruce(padres[0], padres[1])
            if random.random() < 0.3: #probabilidad de mutacion
                hujo = mutacion(hijo)
            nueva_poblacion.append(hijo)

        poblacion = nueva_poblacion

    mejor = max(poblacion, key=funcion_objetivo)
    return mejor, funcion_objetivo(mejor)

#ejemplo de la ejecucion del algoritmo genetico
mejor_solucion, valor = algoritmo_genetico()
print("Mejor solución encontrada:", mejor_solucion)
print("Valor de la función:", valor)