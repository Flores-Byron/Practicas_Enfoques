# Estados y observaciones
estados = ["Soleado","Lluvioso"]
observaciones = ["Paraguas","SinParaguas"]

# Distribución inicial
pi = {"Soleado":0.5,"Lluvioso":0.5}

# Transiciones
transiciones = {
    "Soleado":{"Soleado":0.8,"Lluvioso":0.2},
    "Lluvioso":{"Soleado":0.3,"Lluvioso":0.7}
}

# Emisiones
emisiones = {
    "Soleado":{"Paraguas":0.1,"SinParaguas":0.9},
    "Lluvioso":{"Paraguas":0.8,"SinParaguas":0.2}
}

# Evidencia observada
evidencia = ["Paraguas","SinParaguas","Paraguas"]

# Forward
def forward(evidencia):
    alpha = [{} for _ in range(len(evidencia))]
    for s in estados:
        alpha[0][s] = pi[s] * emisiones[s][evidencia[0]]
    for t in range(1,len(evidencia)):
        for s in estados:
            alpha[t][s] = sum(alpha[t-1][s_prev]*transiciones[s_prev][s] for s_prev in estados) * emisiones[s][evidencia[t]]
    return alpha

# Backward
def backward(evidencia):
    beta = [{} for _ in range(len(evidencia))]
    for s in estados:
        beta[-1][s] = 1
    for t in range(len(evidencia)-2,-1,-1):
        for s in estados:
            beta[t][s] = sum(transiciones[s][s_next]*emisiones[s_next][evidencia[t+1]]*beta[t+1][s_next] for s_next in estados)
    return beta

# Forward-Backward
alpha = forward(evidencia)
beta = backward(evidencia)

# Probabilidad posterior de cada estado en cada tiempo
posterior = []
for t in range(len(evidencia)):
    normalizador = sum(alpha[t][s]*beta[t][s] for s in estados)
    posterior.append({s:(alpha[t][s]*beta[t][s])/normalizador for s in estados})

print("Distribución posterior en cada tiempo:")
for t,p in enumerate(posterior):
    print(f"Tiempo {t+1}: {p}")
