import random

#estados posibles
estados = ["A", "B"]

#probabilidades de transicion
transiciones = {
    "A": {"A": 0.7, "B": 0.3},
    "B": {"A": 0.4, "B": 0.6}
}

# Modelo de observación (sensor con ruido)
observaciones = ["ve_A", "ve_B"]
modelo_observacion = {
    "A": {"ve_A": 0.9, "ve_B": 0.1},
    "B": {"ve_A": 0.2, "ve_B": 0.8}
}

#creencia inicial
creencia = {"A": 0.5, "B": 0.5}

def actualizar_creencia(creencia, observacion):
    nueva_creencia = {}
    for s in estados:
        #prediccion: transicion desde estados anteriores
        pred = sum(creencia[s_prev] * transiciones[s_prev][s] for s_prev in estados)
        #incorporar observacion
        nueva_creencia[s] = pred * modelo_observacion[s][observacion]
    #normalizar
    total = sum(nueva_creencia.values())
    if total == 0:
        return creencia
    for s in nueva_creencia:
        nueva_creencia[s] /= total
    return nueva_creencia

#simulacion de 5 pasos
print("Creencia inicial:", creencia)
for t in range(1, 6):
    obs = random.choices(observaciones, weights=[0.5,0.5])[0]
    creencia = actualizar_creencia(creencia, obs)
    print(f"Paso {t}, observación: {obs}, creencia: {creencia}")