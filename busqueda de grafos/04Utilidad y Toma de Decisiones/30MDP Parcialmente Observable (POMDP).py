import random

# Estados posibles
estados = ["A", "B"]

# Acciones
acciones = ["buscar_A", "buscar_B"]

# Recompensas
recompensas = {"A": {"buscar_A": 10, "buscar_B": -1},
               "B": {"buscar_B": 10, "buscar_A": -1}}

# Observaciones (sensor con ruido)
observaciones = ["ve_A", "ve_B"]
modelo_observacion = {
    "A": {"ve_A": 0.8, "ve_B": 0.2},
    "B": {"ve_A": 0.3, "ve_B": 0.7}
}

# Creencia inicial (50% en cada habitación)
creencia = {"A": 0.5, "B": 0.5}

def actualizar_creencia(creencia, observacion):
    nueva_creencia = {}
    for s in estados:
        p_obs = modelo_observacion[s][observacion]
        nueva_creencia[s] = creencia[s] * p_obs
    total = sum(nueva_creencia.values())
    if total == 0:
        return creencia  # evitar división por cero
    for s in nueva_creencia:
        nueva_creencia[s] /= total
    return nueva_creencia

def utilidad_esperada(creencia, accion):
    valor = 0
    for s in estados:
        valor += creencia[s] * recompensas[s][accion]
    return valor

# Simulación
print("Creencia inicial:", creencia)

# El sensor da una observación
observacion = random.choices(observaciones, weights=[0.5,0.5])[0]
creencia = actualizar_creencia(creencia, observacion)

# Decisión óptima según la creencia
mejor_accion = max(acciones, key=lambda a: utilidad_esperada(creencia, a))

print("Observación recibida:", observacion)
print("Nueva creencia:", creencia)
print("Mejor acción según la creencia:", mejor_accion)
