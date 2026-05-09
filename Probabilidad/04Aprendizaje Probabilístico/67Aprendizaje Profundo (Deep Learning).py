import numpy as np

# Datos de ejemplo: entradas y salidas esperadas
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[0]])  # XOR

# Inicialización de pesos
np.random.seed(42)
W1 = np.random.randn(2,4)   # capa oculta
W2 = np.random.randn(4,1)   # capa salida

def sigmoid(x): return 1/(1+np.exp(-x))
def sigmoid_deriv(x): return x*(1-x)

# Entrenamiento
for _ in range(10000):
    # Forward
    z1 = X.dot(W1)
    a1 = sigmoid(z1)
    z2 = a1.dot(W2)
    a2 = sigmoid(z2)

    # Backprop
    error = y - a2
    d2 = error * sigmoid_deriv(a2)
    d1 = d2.dot(W2.T) * sigmoid_deriv(a1)

    # Actualizar pesos
    W2 += a1.T.dot(d2)*0.1
    W1 += X.T.dot(d1)*0.1

print("Predicciones:")
print(a2.round(3))
