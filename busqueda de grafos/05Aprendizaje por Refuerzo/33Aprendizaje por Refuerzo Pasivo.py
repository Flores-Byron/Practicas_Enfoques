# Estados representados como coordenadas
estados = [(0,0), (0,1), (1,0), (1,1)]
acciones = ["derecha", "abajo"]

# Recompensas
recompensas = {(0,0): 0, (0,1): 0, (1,0): 0, (1,1): 10}

# Transiciones deterministas
def mover(estado, accion):
    x, y = estado
    if accion == "derecha":
        y = min(y+1, 1)
    elif accion == "abajo":
        x = min(x+1, 1)
    return (x,y)

transiciones = {s: {a: {mover(s,a): 1.0} for a in acciones} for s in estados}

gamma = 0.9

# Política fija: derecha si está en fila 0, abajo si está en columna 1
politica = {
    (0,0): "derecha",
    (0,1): "abajo",
    (1,0): "derecha",
    (1,1): "abajo"  # aunque ya está en meta
}

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

print("Política fija evaluada:", politica)
print("Valores de los estados:", valores)
