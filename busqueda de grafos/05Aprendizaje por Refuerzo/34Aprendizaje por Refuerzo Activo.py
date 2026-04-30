import random

#estados y acciones
estados = [0, 1, 2]
acciones = ["avanzar", "esperar"]

#recompensas
recompensas = {0: 0, 1: 0, 2: 10}

#transiciones deterministas
transiciones = {
    0: {"avanzar": 1, "esperar": 0},
    1: {"avanzar": 2, "esperar": 1},
    2: {"avanzar": 2, "esperar": 2}
}

#parametros
gamma = 0.9
alpha = 0.1
epsilon = 0.2 #probabilidad de explorar

#inicializar q-valores
Q = {(s ,a): 0 for s in estados for a in acciones}

def elegir_accion(s):
    if random.random() < epsilon:
        return random.choice(acciones)
    else:
        #esploracion con mayor Q
        return max(acciones, key=lambda a: Q[(s, a)])
    
#entrenamiento
for episodio in range(100):
    estado = 0
    while estado != 2: #hasta llegar a la meta
        accion = elegir_accion(estado)
        siguiente = transiciones[estado][accion]
        recompensa = recompensas[siguiente]
        #actualizacion Q-learning
        Q[(estado, accion)] += alpha * (recompensa + gamma * max(Q[(siguiente, a)] for a in acciones) - Q[(estado, accion)])
        estado = siguiente
    
#derivar politica optima
politica = {s: max(acciones, key=lambda a: Q[(s, a)]) for s in estados}

print("Q-valores aprendidos:", Q)
print("Política óptima aprendida:", politica)