import math
import random

def temple_simulado(funcion_objetivo, generar_vecino, estado_inicial, temperatura_inicial=100, enfriamiento=0.95, iteraciones=1000):
    estado_actual = estado_inicial
    valor_actual = funcion_objetivo(estado_actual)
    mejor_estado = estado_actual
    mejor_valor = valor_actual
    temperatura = temperatura_inicial

    for _ in range(iteraciones):
        # Generar un vecino aleatorio
        vecino = generar_vecino(estado_actual)
        valor_vecino = funcion_objetivo(vecino)

        # Diferencia de energía (valor)
        delta = valor_vecino - valor_actual

        # Aceptar siempre si es mejor, o con probabilidad si es peor
        if delta > 0 or random.random() < math.exp(delta / temperatura):
            estado_actual = vecino
            valor_actual = valor_vecino

            # Actualizar mejor solución global
            if valor_actual > mejor_valor:
                mejor_estado = estado_actual
                mejor_valor = valor_actual

        # Reducir la temperatura
        temperatura *= enfriamiento

    return mejor_estado, mejor_valor

# Ejemplo de uso:
# Función objetivo: maximizar -(x-5)^2 + 25 (máximo en x=5)
def funcion_objetivo(x):
    return -(x-5)**2 + 25

# Generador de vecino: movimiento aleatorio alrededor del estado actual
def generar_vecino(x):
    return x + random.choice([-1, 1])

estado_inicial = random.randint(0, 10)
resultado, valor = temple_simulado(funcion_objetivo, generar_vecino, estado_inicial)

print("Estado inicial:", estado_inicial)
print("Mejor estado encontrado:", resultado)
print("Valor de la función:", valor)
