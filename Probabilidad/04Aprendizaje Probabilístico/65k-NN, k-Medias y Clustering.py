import numpy as np
from collections import Counter

# Datos simples
X = np.array([[1],[2],[1.5],[8],[9],[8.5]])
y = ["A","A","A","B","B","B"]  # etiquetas para k-NN

# k-NN clasificación
def knn_predict(x, X, y, k=3):
    distancias = [(abs(x - X[i][0]), y[i]) for i in range(len(X))]
    vecinos = sorted(distancias)[:k]
    clases = [clase for _, clase in vecinos]
    return Counter(clases).most_common(1)[0][0]

print("Clasificación k-NN para 2.2:", knn_predict(2.2, X, y))

# k-Means clustering (simplificado)
def kmeans(datos, k=2, iteraciones=5):
    centroides = np.random.choice(datos.flatten(), k, replace=False)
    for _ in range(iteraciones):
        grupos = [[] for _ in range(k)]
        for x in datos.flatten():
            idx = np.argmin([abs(x-c) for c in centroides])
            grupos[idx].append(x)
        centroides = [np.mean(g) if g else c for g,c in zip(grupos,centroides)]
    return centroides, grupos

centroides, grupos = kmeans(X, k=2)
print("Clusters k-Means:", grupos)
