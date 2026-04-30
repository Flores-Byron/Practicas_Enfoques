import random

# Estados
estados = [(0,0), (0,1), (1,0), (1,1)]
acciones = ["arriba", "abajo", "izquierda", "derecha"]

# Recompensas
recompensas = {(0,0): 0, (0,1): 0, (1,0): 0, (1,1): 10}

# Función de transición
def mover(estado, accion):
    x, y = estado
    if accion == "arriba":    x = max(x-1,0)
    if accion == "abajo":     x = min(x+1,1)
    if accion == "izquierda": y = max(y-1,0)
    if accion == "derecha":   y = min(y+1,1)
    return (x,y)

# Parámetros
gamma = 0.9
alpha = 0.1
epsilon = 0.2
Q = {(s,a): 0 for s in estados for a in acciones}

def elegir_accion(s):
    if random.random() < epsilon:
        return random.choice(acciones)  # exploración
    else:
        return max(acciones, key=lambda a: Q[(s,a)])  # explotación

# Entrenamiento
for episodio in range(200):
    estado = (0,0)
    while estado != (1,1):
        accion = elegir_accion(estado)
        siguiente = mover(estado, accion)
        recompensa = recompensas[siguiente]
        Q[(estado,accion)] += alpha * (recompensa + gamma * max(Q[(siguiente,a)] for a in acciones) - Q[(estado,accion)])
        estado = siguiente

# Derivar política óptima
politica = {s: max(acciones, key=lambda a: Q[(s,a)]) for s in estados}

print("Q-valores aprendidos:")
for k,v in Q.items():
    print(k, ":", round(v,2))
print("\nPolítica óptima:", politica)
