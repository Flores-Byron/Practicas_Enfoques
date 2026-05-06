import itertools

# Probabilidades
p_clases = {True: 0.7, False: 0.3}
p_lluvia_dado_clases = {True: {True: 0.4, False: 0.6},
                        False: {True: 0.2, False: 0.8}}
p_paraguas_dado = {(True,True): 0.9, (True,False): 0.1,
                   (False,True): 0.5, (False,False): 0.5}

# Evidencia: C=True
evidencia = {"C": True}

# Enumeración de todas las combinaciones de L y P
valores = []
for L,P in itertools.product([True,False],[True,False]):
    prob = p_clases[evidencia["C"]] * p_lluvia_dado_clases[evidencia["C"]][L]
    prob *= p_paraguas_dado[(evidencia["C"],L)] if P else (1-p_paraguas_dado[(evidencia["C"],L)])
    valores.append((P,prob))

# Normalización
total = sum(prob for _,prob in valores)
posterior = {P: prob/total for P,prob in valores}

print("Distribución posterior P(P|C=Sí):", posterior)
