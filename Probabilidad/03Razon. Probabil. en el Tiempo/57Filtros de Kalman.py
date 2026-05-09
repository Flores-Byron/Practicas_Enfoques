import random

# Parámetros del modelo
A = [[1,1],[0,1]]   # transición: x_t = x_{t-1} + v
H = [[1,0]]         # observamos solo la posición
Q = [[0.001,0],[0,0.001]]  # ruido del proceso
R = [[0.1]]         # ruido de la medición

# Estado inicial
x = [0,1]   # posición=0, velocidad=1
P = [[1,0],[0,1]]

def kalman_filter(z_mediciones):
    global x,P
    resultados = []
    for z in z_mediciones:
        # Predicción
        x_pred = [A[0][0]*x[0]+A[0][1]*x[1],
                  A[1][0]*x[0]+A[1][1]*x[1]]
        P_pred = [[P[0][0]+Q[0][0], P[0][1]+Q[0][1]],
                  [P[1][0]+Q[1][0], P[1][1]+Q[1][1]]]

        # Ganancia de Kalman (simplificada para 1D observación)
        S = P_pred[0][0] + R[0][0]
        K = [P_pred[0][0]/S, P_pred[1][0]/S]

        # Actualización
        y = z - x_pred[0]  # innovación
        x = [x_pred[0] + K[0]*y, x_pred[1] + K[1]*y]
        resultados.append(x)
    return resultados

# Simulación de mediciones con ruido
mediciones = [i + random.gauss(0,0.3) for i in range(10)]
estimaciones = kalman_filter(mediciones)

print("Mediciones:", mediciones)
print("Estimaciones:", estimaciones)
