import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Datos simulados con ruido
datos = np.sin(np.arange(0, 6*np.pi, 0.1)) + np.random.randn(189) * 0.2
datos_df = pd.DataFrame(datos, columns=['y'])

# Suavizado con media móvil
suavizado = datos_df.rolling(window=5).mean().dropna().values.flatten()

# División en entrenamiento y prueba
datos_entrenamiento = datos[:80]
datos_prueba = datos[80:]

# Modelo de predicción (regresión lineal)
X_entrenamiento = np.arange(len(datos_entrenamiento)).reshape(-1, 1)
modelo = LinearRegression().fit(X_entrenamiento, datos_entrenamiento.reshape(-1, 1))

# Predicciones
X_prueba = np.arange(len(datos_entrenamiento), len(datos)).reshape(-1, 1)
y_pred = modelo.predict(X_prueba).flatten()

# Visualización
plt.plot(datos, label='Datos originales')
plt.plot(np.arange(2, len(suavizado)+2), suavizado, label='Suavizado')
plt.plot(np.arange(80, len(datos)), y_pred, label='Predicción')
plt.legend()
plt.show()
