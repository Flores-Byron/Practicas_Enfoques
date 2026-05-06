import random

# Distribuciones
p_genetica = {True:0.3, False:0.7}
p_enfermedad_dado_genetica = {True:{True:0.6, False:0.4},
                              False:{True:0.1, False:0.9}}
p_sintoma_dado_enfermedad = {True:{True:0.8, False:0.2},
                             False:{True:0.3, False:0.7}}

def ponderacion_verosimilitud(n=2000, evidencia={"Sintoma":True}):
    muestras = []
    for _ in range(n):
        peso = 1.0
        
        # Genética (muestreo normal)
        G = random.random() < p_genetica[True]
        
        # Enfermedad (condicionado a genética)
        E = random.random() < p_enfermedad_dado_genetica[G][True]
        
        # Síntoma (evidencia)
        S = evidencia["Sintoma"]
        peso *= p_sintoma_dado_enfermedad[E][S]
        
        muestras.append((G,E,S,peso))
    
    # Estimación posterior
    peso_total = sum(m[-1] for m in muestras)
    prob_enfermedad = sum(m[-1] for m in muestras if m[1]) / peso_total
    return prob_enfermedad

print("Probabilidad de enfermedad dado síntoma=Sí:", round(ponderacion_verosimilitud(2000),3))
