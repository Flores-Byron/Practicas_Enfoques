# Probabilidad de lluvia
prob_lluvia = 0.4

# Utilidades:
# Llevar paraguas: incomodidad (-1), pero evita mojarse
# No llevar paraguas: si llueve (-10), si no llueve (+5)
utilidades = {
    "llevar": {"lluvia": -1, "no_lluvia": -1},   # incomodidad constante
    "no_llevar": {"lluvia": -10, "no_lluvia": 5}
}

def utilidad_esperada(accion):
    return (prob_lluvia * utilidades[accion]["lluvia"] +
            (1 - prob_lluvia) * utilidades[accion]["no_lluvia"])

acciones = ["llevar", "no_llevar"]
mejor_accion = max(acciones, key=utilidad_esperada)

print("Utilidad esperada de cada acción:")
for a in acciones:
    print(f"{a}: {utilidad_esperada(a)}")

print("Mejor decisión según la red de decisión:", mejor_accion)
