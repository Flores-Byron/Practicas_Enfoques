# Probabilidades simples
p_clases = 0.7
p_lluvia_dado_clases = 0.4
p_paraguas_dado_clases_lluvia = 0.9

# Aplicando la regla de la cadena
p_conjunta = p_clases * p_lluvia_dado_clases * p_paraguas_dado_clases_lluvia

print("Probabilidad conjunta P(C,L,P):", round(p_conjunta,3))