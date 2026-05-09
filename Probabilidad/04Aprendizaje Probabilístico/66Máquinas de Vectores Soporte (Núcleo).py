import numpy as np

# Datos simulados
X1 = np.random.randn(20,2) + [2,2]
X2 = np.random.randn(20,2) + [-2,-2]
X = np.vstack((X1,X2))
y = np.array([1]*20 + [-1]*20)

# Kernel RBF
def rbf_kernel(x, z, gamma=0.5):
    return np.exp(-gamma*np.linalg.norm(x-z)**2)

# Matriz de kernel
K = np.zeros((len(X),len(X)))
for i in range(len(X)):
    for j in range(len(X)):
        K[i,j] = rbf_kernel(X[i],X[j])

# Entrenamiento simplificado (dual variables α)
# Aquí se usa un pseudo-entrenamiento con valores fijos para ilustrar
alpha = np.random.rand(len(X))
w = np.sum(alpha[:,None]*y[:,None]*X, axis=0)

# Predicción
def predict(x):
    s = 0
    for i in range(len(X)):
        s += alpha[i]*y[i]*rbf_kernel(X[i],x)
    return np.sign(s)

nuevo = np.array([0,0])
print("Clase predicha para (0,0):", predict(nuevo))
