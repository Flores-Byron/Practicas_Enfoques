'''
Reconocimiento de "voz" simplificado con HMM + Viterbi
Versión modificada (misma función, parámetros distintos)
'''

# ====================== MODELOS ========================================

# Estados ocultos (fonemas simplificados)
ESTADOS = ['Q1', 'Q2', 'Q3']

# Observaciones (sonidos simplificados)
OBSERVACIONES = ['a', 'o', 'i']

# Modelo para palabra "HOLA"
HMM_HOLA = {
    'PI': {'Q1': 1.0, 'Q2': 0.0, 'Q3': 0.0},
    'TRANSICION': {
        'Q1': {'Q1': 0.2, 'Q2': 0.8, 'Q3': 0.0},
        'Q2': {'Q1': 0.0, 'Q2': 0.3, 'Q3': 0.7},
        'Q3': {'Q1': 0.0, 'Q2': 0.0, 'Q3': 1.0}
    },
    'EMISION': {
        'Q1': {'o': 0.7, 'a': 0.2, 'i': 0.1},
        'Q2': {'o': 0.3, 'a': 0.6, 'i': 0.1},
        'Q3': {'o': 0.2, 'a': 0.2, 'i': 0.6}
    }
}

# Modelo para palabra "ADIOS"
HMM_ADIOS = {
    'PI': {'Q1': 1.0, 'Q2': 0.0, 'Q3': 0.0},
    'TRANSICION': {
        'Q1': {'Q1': 0.3, 'Q2': 0.7, 'Q3': 0.0},
        'Q2': {'Q1': 0.0, 'Q2': 0.2, 'Q3': 0.8},
        'Q3': {'Q1': 0.0, 'Q2': 0.0, 'Q3': 1.0}
    },
    'EMISION': {
        'Q1': {'a': 0.6, 'o': 0.3, 'i': 0.1},
        'Q2': {'i': 0.6, 'a': 0.3, 'o': 0.1},
        'Q3': {'o': 0.6, 'a': 0.2, 'i': 0.2}
    }
}

# ====================== VITERBI ========================================

def viterbi(secuencia, modelo):
    estados = ESTADOS
    PI = modelo['PI']
    A = modelo['TRANSICION']
    B = modelo['EMISION']

    V = [{}]
    path = {}

    # Inicialización
    for estado in estados:
        V[0][estado] = PI[estado] * B[estado][secuencia[0]]
        path[estado] = [estado]

    # Recursión
    for t in range(1, len(secuencia)):
        V.append({})
        new_path = {}
        for estado_actual in estados:
            (prob, estado_prev) = max(
                (V[t-1][e] * A[e][estado_actual] * B[estado_actual][secuencia[t]], e)
                for e in estados
            )
            V[t][estado_actual] = prob
            new_path[estado_actual] = path[estado_prev] + [estado_actual]
        path = new_path

    # Resultado final
    (prob, estado_final) = max((V[-1][e], e) for e in estados)
    return prob, path[estado_final]

# ====================== RECONOCIMIENTO =================================

def reconocer(secuencia):
    prob_hola, _ = viterbi(secuencia, HMM_HOLA)
    prob_adios, _ = viterbi(secuencia, HMM_ADIOS)

    print("\nSecuencia:", secuencia)
    print("Probabilidad HOLA:", prob_hola)
    print("Probabilidad ADIOS:", prob_adios)

    if prob_hola > prob_adios:
        print("→ Palabra reconocida: HOLA")
    else:
        print("→ Palabra reconocida: ADIOS")

# ====================== EJECUCIÓN ======================================

secuencia = ['o','a','i']   # fonética simplificada de "HOLA"
secuencia2 = ['a','i','o']  # fonética simplificada de "ADIOS"

reconocer(secuencia)
reconocer(secuencia2)
