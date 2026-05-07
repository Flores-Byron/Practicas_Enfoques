import numpy as np

# Estados ocultos: 0 = Codificante, 1 = No codificante
# Observaciones: A=0, C=1, G=2, T=3

# Probabilidades iniciales
pi = np.array([0.5, 0.5])

# Matriz de transición
A = np.array([
    [0.9, 0.1],  # Codificante -> Codificante, No codificante
    [0.2, 0.8]   # No codificante -> Codificante, No codificante
])

# Matriz de emisión (probabilidad de nucleótido dado el estado)
B = np.array([
    [0.3, 0.2, 0.3, 0.2],  # Codificante -> A, C, G, T
    [0.25, 0.25, 0.25, 0.25]  # No codificante -> distribución uniforme
])

# Secuencia observada (ejemplo: A, G, C, T, A)
observaciones = [0, 2, 1, 3, 0]

N = len(observaciones)
alpha = np.zeros((N, len(pi)))
beta = np.zeros((N, len(pi)))

# Paso hacia adelante
alpha[0] = pi * B[:, observaciones[0]]
for t in range(1, N):
    for j in range(len(pi)):
        alpha[t, j] = B[j, observaciones[t]] * np.sum(alpha[t-1] * A[:, j])

# Paso hacia atrás
beta[-1] = 1
for t in range(N-2, -1, -1):
    for i in range(len(pi)):
        beta[t, i] = np.sum(A[i, :] * B[:, observaciones[t+1]] * beta[t+1])

# Probabilidad posterior
posterior = (alpha * beta) / np.sum(alpha * beta, axis=1, keepdims=True)

print("Probabilidades posteriores de estados ocultos:")
for t in range(N):
    print(f"Posición {t+1}: Codificante={posterior[t,0]:.3f}, No codificante={posterior[t,1]:.3f}")
