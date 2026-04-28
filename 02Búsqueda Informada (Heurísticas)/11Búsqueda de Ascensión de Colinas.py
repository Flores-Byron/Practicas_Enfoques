import random

def ascension_colinas(funcion_objetivo, vecinos, estado_inicial, max_iter=100):
    estado_actual = estado_inicial
    valor_actual = funcion_objetivo(estado_actual)

    for h in range(max_iter):
        #generar vecinos del estado actual
        list_vecinos = vecinos(estado_actual)
        if not list_vecinos:
            break

        #evaluar vecinos y elegir el mejor
        mejor_vecino = max(list_vecinos, key=funcion_objetivo)
        mejor_valor = funcion_objetivo(mejor_vecino)

        #si el vecino es mejor que el estado actual, avanzar
        if mejor_vecino> valor_actual:
            estado_actual, valor_actual = mejor_vecino, mejor_valor
        else:
            # no hay mejor vecino, se detiene
            break
    return estado_actual, valor_actual

#Ejmplo de uso
#Funcion objetivo: maximizar el valor de x^2
def funcion_objetivo(x):
    return -(x - 3)**2 + 9 #el maximo en x=3

#generador de vecinos: pequeños pasos alrededor del estado actual
def vecinos(x):
    return [x - 1, x + 1]

estado_inicial = random.randint(-10, 10)
resultado, valor = ascension_colinas(funcion_objetivo, vecinos, estado_inicial)

print("Estado inicial:", estado_inicial)
print("Mejor estado encontrado:", resultado)
print("Valor de la función:", valor)