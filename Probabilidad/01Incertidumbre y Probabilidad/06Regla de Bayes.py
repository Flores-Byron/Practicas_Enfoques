# Probabilidad a priori
p_enfermedad = 0.02
p_sano = 0.98

# Verosimilitudes
p_positivo_si_enfermo = 0.9
p_positivo_si_sano = 0.1

# Evidencia: resultado positivo
p_positivo = p_enfermedad*p_positivo_si_enfermo + p_sano*p_positivo_si_sano

# Probabilidad posterior
p_enfermedad_dado_positivo = (p_positivo_si_enfermo*p_enfermedad) / p_positivo

print("Probabilidad a priori:", p_enfermedad)
print("Probabilidad posterior dado positivo:", round(p_enfermedad_dado_positivo,3))
