import numpy as np
import matplotlib.pyplot as plt
import statsmodels.tsa.stattools as sts

# Fijamos la semilla para reproducibilidad
np.random.seed(42)

# Número de observaciones
n = 200

# Simulación de un proceso estacionario: ruido blanco
# Media = 0, desviación estándar = 1
ruido_blanco = np.random.normal(loc=0, scale=1, size=n)

# Graficar la serie temporal
plt.figure(figsize=(10,4))
plt.plot(ruido_blanco, label="Ruido blanco")
plt.title("Ejemplo de Proceso Estacionario")
plt.xlabel("Tiempo")
plt.ylabel("Valor")
plt.legend()
plt.show()

# Prueba de Dickey-Fuller Aumentada (ADF) para verificar estacionariedad
resultado_adf = sts.adfuller(ruido_blanco)

print("Estadístico ADF:", resultado_adf[0])
print("Valor p:", resultado_adf[1])
