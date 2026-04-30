# Estados y acciones
estados = [0, 1, 2]
acciones = ["avanzar", "esperar"]

# Recompensas
recompensas = {0: 0, 1: 0, 2: 10}

# Transiciones probabilísticas
transiciones = {
    0: {"avanzar": {1: 1.0}, "esperar": {0: 1.0}},
    1: {"avanzar": {2: 1.0}, "esperar": {1: 1.0}},
    2: {"avanzar": {2: 1.0}, "esperar": {2: 1.0}}
}

gamma = 0.9

# Evaluar una política simple: avanzar siempre
politica = {0: "avanzar", 1: "avanzar", 2: "esperar"}

def evaluar_politica(politica, iteraciones=10):
    V = {s: 0 for s in estados}
    for _ in range(iteraciones):
        for s in estados:
            a = politica[s]
            valor = 0
            for s2, p in transiciones[s][a].items():
                valor += p * (recompensas[s2] + gamma * V[s2])
            V[s] = valor
    return V

valores = evaluar_politica(politica)

print("Política evaluada:", politica)
print("Valores de los estados:", valores)
