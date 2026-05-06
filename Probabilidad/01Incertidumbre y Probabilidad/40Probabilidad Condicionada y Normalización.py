# Creencias iniciales
p_A = 0.5
p_B = 0.5

# Modelo de observación
p_obs_A = 0.8  # probabilidad de ver A si realmente está en A
p_obs_B = 0.3  # probabilidad de ver A si realmente está en B

# Evidencia: observamos "ve_A"
no_norm_A = p_obs_A * p_A
no_norm_B = p_obs_B * p_B

# Normalización
total = no_norm_A + no_norm_B
p_A_dado_obs = no_norm_A / total
p_B_dado_obs = no_norm_B / total

print("Probabilidad condicionada normalizada:")
print("P(A|ve_A) =", round(p_A_dado_obs,3))
print("P(B|ve_A) =", round(p_B_dado_obs,3))
