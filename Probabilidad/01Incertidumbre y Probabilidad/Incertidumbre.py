import random

# Probabilidad estimada de lluvia
p_lluvia = 0.4

# Utilidades
utilidades = {
    "llevar": {"lluvia": 5, "no_lluvia": 1},
    "no_llevar": {"lluvia": -5, "no_lluvia": 10}
}

def decision(p_lluvia):
    # Valor esperado de cada acción
    valor_llevar = p_lluvia*utilidades["llevar"]["lluvia"] + (1-p_lluvia)*utilidades["llevar"]["no_lluvia"]
    valor_no = p_lluvia*utilidades["no_llevar"]["lluvia"] + (1-p_lluvia)*utilidades["no_llevar"]["no_lluvia"]
    return "llevar" if valor_llevar > valor_no else "no_llevar"

print("Decisión óptima bajo incertidumbre:", decision(p_lluvia))
