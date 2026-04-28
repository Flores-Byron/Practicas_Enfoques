import random 

def busqueda_online(funcion_objetivo, generar_vecinos, estado_inicial, max_iter=50):
    estado_actual = estado_inicial
    mejor_estado = estado_actual
    mejor_valor = funcion_objetivo(estado_actual)

    for _ in range(max_iter):
        vecinos = generar_vecinos(estado_actual)
        if not vecinos:
            break

        #selccionar vecino aleatorio con la ecploracion online
        vecino = random.choice(vecinos)
        valor_vecino = funcion_objetivo(vecino)

        #actualizar si es que mejor
        if valor_vecino > mejor_valor:
            mejor_estado = vecino
            mejor_valor = valor_vecino

        #avanzar al vecino aunque no sea mejor
        estado_actual = vecino

    return mejor_estado, mejor_valor

#ejemplo de uso
#funcion objetivo:
def funcion_objetivo(x):
    return -(x-8)**2 + 40 #maximo en x=8

#generador de vecinos: 
def generar_vecinos(x):
    return [x-1, x+1]

estado_inicial = random.randint(0, 15)
resultado, valor = busqueda_online(funcion_objetivo, generar_vecinos, estado_inicial)

print("Estado inicial:", estado_inicial)
print("Mejor estado encontrado:", resultado)
print("Valor de la función:", valor)