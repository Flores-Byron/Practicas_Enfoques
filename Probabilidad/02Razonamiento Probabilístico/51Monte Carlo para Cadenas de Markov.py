import random
import math

def metropolis_hastings(n=10000):
    muestras = []
    x = 0  # estado inicial
    for _ in range(n):
        # Propuesta: vecino cercano
        x_propuesto = x + random.uniform(-1,1)
        
        # Densidad objetivo (Normal estándar)
        p_x = math.exp(-x**2/2)
        p_xp = math.exp(-x_propuesto**2/2)
        
        # Aceptación
        alpha = min(1, p_xp/p_x)
        if random.random() < alpha:
            x = x_propuesto
        muestras.append(x)
    return muestras

muestras = metropolis_hastings(10000)
print("Primeras 10 muestras:", muestras[:10])