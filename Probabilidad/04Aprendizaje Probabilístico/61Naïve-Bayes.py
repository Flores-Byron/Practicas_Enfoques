from collections import defaultdict

# Dataset simple
dataset = [
    ("oferta descuento gratis", "spam"),
    ("compra ahora oferta", "spam"),
    ("reunión mañana proyecto", "no_spam"),
    ("agenda reunión equipo", "no_spam")
]

# Entrenamiento
conteo_palabras = {"spam":defaultdict(int), "no_spam":defaultdict(int)}
conteo_clases = {"spam":0, "no_spam":0}

for texto, clase in dataset:
    conteo_clases[clase] += 1
    for palabra in texto.split():
        conteo_palabras[clase][palabra] += 1

# Clasificación con Naïve Bayes
def clasificar(texto):
    palabras = texto.split()
    resultados = {}
    for clase in ["spam","no_spam"]:
        prob = conteo_clases[clase]/sum(conteo_clases.values())
        for palabra in palabras:
            prob *= (conteo_palabras[clase][palabra]+1) / (sum(conteo_palabras[clase].values())+len(palabras))
        resultados[clase] = prob
    return max(resultados, key=resultados.get), resultados

# Ejemplo de prueba
mensaje1 = "oferta gratis"
mensaje2 = "reunión proyecto"

print("Mensaje:", mensaje1, "→", clasificar(mensaje1))
print("Mensaje:", mensaje2, "→", clasificar(mensaje2))
