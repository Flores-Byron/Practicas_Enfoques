import random

# Estados y acciones
estados = [0, 1, 2]
acciones = ["avanzar", "esperar"]

# Recompensas
recompensas = {0: 0, 1: 0, 2: 10}

# Transiciones deterministas
transiciones = {
    0: {"avanzar": 1, "esperar": 0},
    1: {"avanzar": 2, "esperar": 1},
    2: {"avanzar": 2, "esperar": 2}
}

# Parámetros
gamma = 0.9
alpha = 0.1
epsilon = 0.3  # 30% de exploración

# Inicializar Q-valores
Q = {(s,a): 0 for s in estados for a in acciones}

def elegir_accion(s):
    if random.random() < epsilon:
        return random.choice(acciones)  # exploración
    else:
        return max(acciones, key=lambda a: Q[(s,a)])  # explotación

# Entrenamiento
for episodio in range(100):
    estado = 0
    while estado != 2:
        accion = elegir_accion(estado)
        siguiente = transiciones[estado][accion]
        recompensa = recompensas[siguiente]
        Q[(estado,accion)] += alpha * (recompensa + gamma * max(Q[(siguiente,a)] for a in acciones) - Q[(estado,accion)])
        estado = siguiente

# Política aprendida
politica = {s: max(acciones, key=lambda a: Q[(s,a)]) for s in estados}

print("Q-valores:", {k: round(v,2) for k,v in Q.items()})
print("Política aprendida:", politica)
