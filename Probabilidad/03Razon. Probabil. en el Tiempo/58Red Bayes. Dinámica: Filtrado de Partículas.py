import random

# Estados posibles (posiciones en el pasillo)
estados = [0,1,2,3,4]

# Inicialización de partículas
def inicializar_particulas(n=100):
    return [random.choice(estados) for _ in range(n)]

# Modelo de transición: movimiento izquierda/derecha
def mover(particula):
    if particula == 0:
        return 1
    elif particula == 4:
        return 3
    else:
        return particula + random.choice([-1,1])

# Modelo de observación: sensor de pared
def prob_observacion(estado, observacion):
    cerca_pared = (estado==0 or estado==4)
    if observacion=="Cerca":
        return 0.8 if cerca_pared else 0.2
    else:
        return 0.2 if cerca_pared else 0.8

# Filtrado de partículas
def filtrado_particulas(evidencias, n=100):
    particulas = inicializar_particulas(n)
    resultados = []
    for obs in evidencias:
        # Predicción
        particulas = [mover(p) for p in particulas]
        # Actualización de pesos
        pesos = [prob_observacion(p,obs) for p in particulas]
        # Normalización
        total = sum(pesos)
        pesos = [w/total for w in pesos]
        # Re-muestreo
        particulas = random.choices(particulas, weights=pesos, k=n)
        resultados.append(particulas)
    return resultados

# Evidencias observadas por el sensor
evidencias = ["Cerca","Lejos","Cerca"]

# Ejecución
resultado = filtrado_particulas(evidencias, n=200)

# Distribución final (frecuencia de estados)
final = resultado[-1]
distribucion = {s:final.count(s)/len(final) for s in estados}
print("Distribución posterior de estados:", distribucion)
