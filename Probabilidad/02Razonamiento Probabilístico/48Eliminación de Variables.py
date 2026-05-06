# Probabilidades a priori
p_genetica = {True: 0.2, False: 0.8}

# Enfermedad depende de genética
p_enfermedad_dado_genetica = {True: {True: 0.6, False: 0.4},
                              False: {True: 0.1, False: 0.9}}

# Fiebre depende de enfermedad
p_fiebre_dado_enfermedad = {True: {True: 0.8, False: 0.2},
                            False: {True: 0.3, False: 0.7}}

# Dolor depende de enfermedad
p_dolor_dado_enfermedad = {True: {True: 0.7, False: 0.3},
                           False: {True: 0.2, False: 0.8}}

# Evidencia: Fiebre=True
evidencia = {"F": True}

# Eliminación de variables G y P
prob_E_true = 0
prob_E_false = 0
for G in [True,False]:
    p_G = p_genetica[G]
    for E in [True,False]:
        p_E = p_enfermedad_dado_genetica[G][E]
        p_F = p_fiebre_dado_enfermedad[E][True]  # evidencia F=True
        # marginalizamos sobre P (dolor de cabeza)
        p_P_total = sum(p_dolor_dado_enfermedad[E][P] for P in [True,False])
        if E:
            prob_E_true += p_G * p_E * p_F * p_P_total
        else:
            prob_E_false += p_G * p_E * p_F * p_P_total

# Normalización
total = prob_E_true + prob_E_false
posterior = {True: prob_E_true/total, False: prob_E_false/total}

print("Distribución posterior P(E|F=Sí):", posterior)