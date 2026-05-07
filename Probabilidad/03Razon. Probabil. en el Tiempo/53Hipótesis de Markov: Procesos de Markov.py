import numpy as np

# Definimos los estados
estados = ["Soleado", "Nublado", "Lluvioso"]

# Definimos la matriz de transición
# Cada fila representa el estado actual y cada columna el estado futuro
matriz_transicion = np.array([
    [0.6, 0.3, 0.1],  # Soleado -> Soleado, Nublado, Lluvioso
    [0.2, 0.5, 0.3],  # Nublado -> Soleado, Nublado, Lluvioso
    [0.1, 0.3, 0.6]   # Lluvioso -> Soleado, Nublado, Lluvioso
])

# Simulación de la cadena de Markov
np.random.seed(42)
n_pasos = 10
estado_actual = 0  # Comenzamos en "Soleado"
historial = [estados[estado_actual]]

for _ in range(n_pasos):
    estado_actual = np.random.choice([0,1,2], p=matriz_transicion[estado_actual])
    historial.append(estados[estado_actual])

print("Simulación del clima:")
print(historial)
