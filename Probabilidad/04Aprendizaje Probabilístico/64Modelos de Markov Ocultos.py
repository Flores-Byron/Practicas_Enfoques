# Estados y observaciones
estados = ["Sano","Enfermo"]
observaciones = ["Fiebre","NoFiebre"]

# Distribución inicial
pi = {"Sano":0.6,"Enfermo":0.4}

# Transiciones
transiciones = {
    "Sano":{"Sano":0.7,"Enfermo":0.3},
    "Enfermo":{"Sano":0.4,"Enfermo":0.6}
}

# Emisiones
emisiones = {
    "Sano":{"Fiebre":0.2,"NoFiebre":0.8},
    "Enfermo":{"Fiebre":0.8,"NoFiebre":0.2}
}

# Evidencia observada
evidencia = ["Fiebre","NoFiebre","Fiebre"]

# Algoritmo hacia adelante
def forward(evidencia):
    alpha = [{} for _ in range(len(evidencia))]
    # Inicialización
    for s in estados:
        alpha[0][s] = pi[s] * emisiones[s][evidencia[0]]
    # Recursión
    for t in range(1,len(evidencia)):
        for s in estados:
            alpha[t][s] = sum(alpha[t-1][s_prev]*transiciones[s_prev][s] for s_prev in estados) * emisiones[s][evidencia[t]]
    return alpha

resultado = forward(evidencia)
print("Probabilidades hacia adelante:", resultado)
