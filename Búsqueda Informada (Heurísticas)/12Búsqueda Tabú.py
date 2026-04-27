import random

def busqueda_tabu(funcion_objetivo, generar_vecinos, estado_inicial, tamaño_tabu=5, max_iter=50):
    estado_actual = estado_inicial
    valor_actual = funcion_objetivo(estado_actual)
    mejor_estado = estado_actual
    mejor_valor = valor_actual

    lista_tabu = []

    for h in range(max_iter):
        vecinos = generar_vecinos(estado_actual)
        mejores_vecino = None
        mejor_valor_vecino = float("-inf")

        for vecino in vecinos:
            if vecino not in lista_tabu:
                valor_vecino = funcion_objetivo(vecino)
                if valor_vecino > mejor_valor_vecino:
                    mejor_valor_vecino = valor_vecino
                    mejor_vecino = vecino

        if mejor_vecino is None:
            break #no hay vecinos validos

        estado_actual = mejor_vecino
        valor_actual = mejor_valor_vecino

        #actualizar mejor solucion global
        if valor_actual > mejor_valor:
            mejor_estado = estado_actual
            mejor_valor = valor_actual
        
        #actualizar lista tabu
        lista_tabu.append(estado_actual)
        if len(lista_tabu) > tamaño_tabu:
            lista_tabu.pop(0)

    return mejor_estado, mejor_valor

#Ejemplo de uso
#Funcion objetivo: maximizar -(x - 5)^2 + 25 (maximo en x = 5)
def funcion_objetivo(x):
    return -(x - 5)**2 + 25

# Generador de vecinos: pasos alrededor del estado actual
def generar_vecinos(x):
    return [x-1, x+1]

estado_inicial = random.randint(0, 10)
resultado, valor = busqueda_tabu(funcion_objetivo, generar_vecinos, estado_inicial)

print("Estado inicial:", estado_inicial)
print("Mejor estado encontrado:", resultado)
print("Valor de la función:", valor)