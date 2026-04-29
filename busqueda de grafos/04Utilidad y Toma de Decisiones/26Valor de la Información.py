#probabilidad de enfermedad
prob_enfermedad = 0.3

#utilidades sin informacion
utilidades = {
    "tratar": {"enfermo": -2, "sano": -2},   # costo fijo del tratamiento
    "no_tratar": {"enfermo": -10, "sano": 0}
}

def utilidad_esperada(accion):
    return (prob_enfermedad * utilidades[accion]["enfermo"]+
            (1 - prob_enfermedad) * utilidades[accion]["sano"])

acciones = ["tratar", "no_tratar"]
mejor_sin_info = max(acciones, key=utilidad_esperada)
utilidad_sin_info = utilidad_esperada(mejor_sin_info)

#con informacion perfecta (prueba diagnostica)
utilidad_con_info = (
    prob_enfermedad * max(utilidades[a]["enfermo"] for a in acciones) +
    (1 - prob_enfermedad) * max(utilidades[a]["sano"] for a in acciones)
)

#restar el costo de la prueba diagnostica
utilidad_con_info -= 1

#valor de la informacion
valor_info = utilidad_con_info - utilidad_sin_info

print("Mejor decisión sin información:", mejor_sin_info, "→ Utilidad:", utilidad_sin_info)
print("Utilidad esperada con información perfecta (incluyendo costo de prueba):", utilidad_con_info)
print("Valor de la información:", valor_info)