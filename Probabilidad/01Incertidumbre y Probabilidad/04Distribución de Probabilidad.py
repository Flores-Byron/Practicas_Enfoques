import random

# Simulación de lanzar un dado
valores = [1,2,3,4,5,6]
probabilidades = {v: 1/6 for v in valores}  # distribución uniforme

# Elegir un valor según la distribución
resultado = random.choices(valores, weights=[probabilidades[v] for v in valores])[0]

print("Distribución:", probabilidades)
print("Resultado del dado:", resultado)
