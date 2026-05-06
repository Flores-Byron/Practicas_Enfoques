# Probabilidad a priori
p_enfermedad = 0.01
p_sano = 0.99

# Verosimilitudes
p_positivo_si_enfermo = 0.95
p_positivo_si_sano = 0.05

# Evidencia: resultado positivo
p_positivo = p_enfermedad*p_positivo_si_enfermo + p_sano*p_positivo_si_sano

# Probabilidad posterior
p_enfermedad_dado_positivo = (p_positivo_si_enfermo*p_enfermedad) / p_positivo

print("Probabilidad a priori de enfermedad:", p_enfermedad)
print("Probabilidad posterior dado positivo:", round(p_enfermedad_dado_positivo,3))