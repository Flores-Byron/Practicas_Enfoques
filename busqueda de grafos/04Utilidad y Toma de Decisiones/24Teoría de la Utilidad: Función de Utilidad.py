#definicion de proyectos con ganancia esperada y riesgos
proyectos = {
    "Proyecto A": {"ganancia": 80, "riesgo": 20},
    "Proyecto B": {"ganancia": 60, "riesgo": 10},
    "Proyecto C": {"ganancia": 100, "riesgo": 50}
}

#funcion de utilidad: balance entre ganancia y riesgo
def utilidad(ganancia, riesgo, alfa=0.7, beta=0.3):
    """
    alfa = peso de la ganancia
    beta = peso del riesgo (penalizacion)
    """
    return alfa * ganancia - beta * riesgo

#evaluacion de cada proyecto
valores_utilidad = {p: utilidad(datos["ganancia"], datos["riesgo"]) for p, datos in proyectos.items()}

#seleccionar el mejor proyecto basado en la utilidad
mejor = max(valores_utilidad, key=valores_utilidad.get)

print("Valores de utilidad:", valores_utilidad)
print("Mejor decisión según la función de utilidad:", mejor)