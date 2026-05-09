"""
Agrupamiento no supervisado con K-Means
Versión alternativa (misma función, diferente estructura)
"""

import random

# ====================== DATOS ==========================================
datos = [1, 2, 1.5, 8, 9, 8.5]
K = 2

# ====================== FUNCIONES ======================================

def inicializar_centroides(datos, k):
    return random.sample(datos, k)

def asignar_clusters(datos, centroides):
    asignaciones = []
    for x in datos:
        distancias = [abs(x - c) for c in centroides]
        asignaciones.append(distancias.index(min(distancias)))
    return asignaciones

def recalcular_centroides(datos, asignaciones, k):
    nuevos = []
    for i in range(k):
        grupo = [x for j,x in enumerate(datos) if asignaciones[j]==i]
        if grupo:
            nuevos.append(sum(grupo)/len(grupo))
        else:
            nuevos.append(0)  # si queda vacío
    return nuevos

def kmeans(datos, k, iteraciones=5):
    centroides = inicializar_centroides(datos, k)
    for it in range(iteraciones):
        asignaciones = asignar_clusters(datos, centroides)
        centroides = recalcular_centroides(datos, asignaciones, k)

        # Mostrar estado
        clusters = {i:[x for j,x in enumerate(datos) if asignaciones[j]==i] for i in range(k)}
        print(f"\nIteración {it+1}:")
        print("Centroides:", centroides)
        print("Clusters:", clusters)
    return centroides

# ====================== EJECUCIÓN ======================================
final_centroides = kmeans(datos, K)
