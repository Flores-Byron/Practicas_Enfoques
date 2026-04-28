import random

def busqueda_haz_local(funcion_objetivo, generar_vecinos, estados_iniciales, k=3, max_iter=50):
    # Lista de estados actuales
    estados = estados_iniciales

    for _ in range(max_iter):
        # Generar todos los vecinos de los estados actuales
        vecinos = []
        for estado in estados:
            vecinos.extend(generar_vecinos(estado))

        # Evaluar todos los vecinos
        vecinos_evaluados = sorted(vecinos, key=funcion_objetivo, reverse=True)

        # Seleccionar los mejores k
        estados = vecinos_evaluados[:k]

    # Devolver el mejor estado encontrado
    mejor_estado = max(estados, key=funcion_objetivo)
    return mejor_estado, funcion_objetivo(mejor_estado)

# Ejemplo de uso:
# Función objetivo: maximizar -(x-5)^2 + 25 (máximo en x=5)
def funcion_objetivo(x):
    return -(x-5)**2 + 25

# Generador de vecinos: pasos alrededor del estado actual
def generar_vecinos(x):
    return [x-1, x+1]

# Estados iniciales aleatorios
estados_iniciales = [random.randint(0, 10) for _ in range(3)]

resultado, valor = busqueda_haz_local(funcion_objetivo, generar_vecinos, estados_iniciales, k=3)

print("Estados iniciales:", estados_iniciales)
print("Mejor estado encontrado:", resultado)
print("Valor de la función:", valor)
