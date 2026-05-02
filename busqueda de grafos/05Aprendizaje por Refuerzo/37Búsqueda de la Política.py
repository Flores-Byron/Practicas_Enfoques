import random

# Estados y acciones
estados = [0, 1, 2]
acciones = ["avanzar", "esperar"]

# Recompensas
recompensas = {0: 0, 1: 0, 2: 10}

# Política parametrizada: probabilidad de avanzar en cada estado
politica = {0: 0.5, 1: 0.5, 2: 0.0}  # inicial

alpha = 0.1  # tasa de aprendizaje
gamma = 0.9  # descuento

def elegir_accion(s):
    if random.random() < politica[s]:
        return "avanzar"
    else:
        return "esperar"

# Entrenamiento con REINFORCE
for episodio in range(200):
    trayectoria = []
    estado = 0
    while estado != 2:
        accion = elegir_accion(estado)
        siguiente = estado if accion=="esperar" else min(estado+1,2)
        recompensa = recompensas[siguiente]
        trayectoria.append((estado,accion,recompensa))
        estado = siguiente
    
    # Calcular retorno acumulado
    G = 0
    for (s,a,r) in reversed(trayectoria):
        G = r + gamma*G
        # Actualizar política (si acción fue avanzar)
        if a=="avanzar":
            politica[s] += alpha * (G - politica[s])

print("Política aprendida:", politica)
