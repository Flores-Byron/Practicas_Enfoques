import numpy as np

# Datos simulados
np.random.seed(42)
datos = np.concatenate([np.random.normal(0,1,50), np.random.normal(5,1,50)])

# Inicialización
mu1, mu2 = -1, 4
sigma1, sigma2 = 1, 1
pi = 0.5

def em_gaussian(datos, iteraciones=10):
    global mu1, mu2, sigma1, sigma2, pi
    for _ in range(iteraciones):
        # E-step: responsabilidades
        p1 = pi * (1/(np.sqrt(2*np.pi)*sigma1)) * np.exp(-(datos-mu1)**2/(2*sigma1**2))
        p2 = (1-pi) * (1/(np.sqrt(2*np.pi)*sigma2)) * np.exp(-(datos-mu2)**2/(2*sigma2**2))
        gamma = p1/(p1+p2)

        # M-step: actualizar parámetros
        mu1 = np.sum(gamma*datos)/np.sum(gamma)
        mu2 = np.sum((1-gamma)*datos)/np.sum(1-gamma)
        sigma1 = np.sqrt(np.sum(gamma*(datos-mu1)**2)/np.sum(gamma))
        sigma2 = np.sqrt(np.sum((1-gamma)*(datos-mu2)**2)/np.sum(1-gamma))
        pi = np.mean(gamma)

    return mu1, mu2, sigma1, sigma2, pi

resultado = em_gaussian(datos, iteraciones=20)
print("Parámetros estimados:", resultado)
