# Estados: 0, 1, 2
estados = [0, 1, 2]
acciones = ["avanzar", "esperar"]

# Recompensas
recompensas = {0: 0, 1: 0, 2: 10}

# Probabilidades de transición
transiciones = {
    0: {"avanzar": {1: 1.0}, "esperar": {0: 1.0}},
    1: {"avanzar": {2: 1.0}, "esperar": {1: 1.0}},
    2: {"avanzar": {2: 1.0}, "esperar": {2: 1.0}}
}

# Parámetros
gamma = 0.9   # factor de descuento
theta = 0.001 # umbral de convergencia

# Inicializar valores
V = {s: 0 for s in estados}

def iteracion_valores():
    while True:
        delta = 0
        for s in estados:
            v = V[s]
            # Evaluar todas las acciones
            valores_accion = []
            for a in acciones:
                valor = 0
                for s2, p in transiciones[s][a].items():
                    valor += p * (recompensas[s2] + gamma * V[s2])
                valores_accion.append(valor)
            V[s] = max(valores_accion)
            delta = max(delta, abs(v - V[s]))
        if delta < theta:
            break
    return V

# Ejecutar iteración de valores
valores_finales = iteracion_valores()

# Derivar política óptima
politica = {}
for s in estados:
    mejor_accion = None
    mejor_valor = -float("inf")
    for a in acciones:
        valor = 0
        for s2, p in transiciones[s][a].items():
            valor += p * (recompensas[s2] + gamma * V[s2])
        if valor > mejor_valor:
            mejor_valor = valor
            mejor_accion = a
    politica[s] = mejor_accion

print("Valores óptimos:", valores_finales)
print("Política óptima:", politica)
