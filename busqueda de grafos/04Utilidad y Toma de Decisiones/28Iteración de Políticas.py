# Estados representados como coordenadas
estados = [(0,0), (0,1), (1,0), (1,1)]
acciones = ["arriba", "abajo", "izquierda", "derecha"]

# Recompensas
recompensas = {(0,0): 0, (0,1): 0, (1,0): 0, (1,1): 10}

# Transiciones deterministas
def mover(estado, accion):
    x, y = estado
    if accion == "arriba":    x, y = max(x-1,0), y
    if accion == "abajo":     x, y = min(x+1,1), y
    if accion == "izquierda": x, y = x, max(y-1,0)
    if accion == "derecha":   x, y = x, min(y+1,1)
    return (x,y)

transiciones = {s: {a: {mover(s,a): 1.0} for a in acciones} for s in estados}

# Parámetros
gamma = 0.9
theta = 0.001

# Inicializar política arbitraria
politica = {s: "derecha" for s in estados}
V = {s: 0 for s in estados}

def evaluar_politica(politica):
    while True:
        delta = 0
        for s in estados:
            v = V[s]
            a = politica[s]
            valor = 0
            for s2, p in transiciones[s][a].items():
                valor += p * (recompensas[s2] + gamma * V[s2])
            V[s] = valor
            delta = max(delta, abs(v - V[s]))
        if delta < theta:
            break

def mejorar_politica(politica):
    estable = True
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
        if mejor_accion != politica[s]:
            politica[s] = mejor_accion
            estable = False
    return estable

def iteracion_politicas():
    while True:
        evaluar_politica(politica)
        if mejorar_politica(politica):
            break
    return politica, V

# Ejecutar
politica_optima, valores_optimos = iteracion_politicas()

print("Valores óptimos:", valores_optimos)
print("Política óptima:", politica_optima)
