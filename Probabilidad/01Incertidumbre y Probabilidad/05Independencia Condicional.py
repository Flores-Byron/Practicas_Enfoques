# Probabilidades
p_lluvia = 0.3
p_coche_mojado_si_lluvia = 0.9
p_coche_mojado_si_no_lluvia = 0.1
p_paraguas_si_lluvia = 0.8
p_paraguas_si_no_lluvia = 0.2

# Condicionalmente independientes dado lluvia
p_coche_mojado_y_paraguas_si_lluvia = p_coche_mojado_si_lluvia * p_paraguas_si_lluvia
p_coche_mojado_y_paraguas_si_no_lluvia = p_coche_mojado_si_no_lluvia * p_paraguas_si_no_lluvia

print("P(coche mojado ∧ paraguas | lluvia) =", round(p_coche_mojado_y_paraguas_si_lluvia,3))
print("P(coche mojado ∧ paraguas | no lluvia) =", round(p_coche_mojado_y_paraguas_si_no_lluvia,3))
