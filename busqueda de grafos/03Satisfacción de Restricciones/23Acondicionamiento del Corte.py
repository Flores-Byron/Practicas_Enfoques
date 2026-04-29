import itertools

# Definición del mapa (grafo de regiones y sus vecinos)
mapa = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D"],
    "D": ["B", "C"]
}

# Colores disponibles
colores = ["Rojo", "Verde", "Azul"]

def es_consistente(asignacion):
    for region, vecinos in mapa.items():
        if region not in asignacion:
            continue
        for vecino in vecinos:
            if vecino in asignacion and asignacion[region] == asignacion[vecino]:
                return False
    return True

def backtracking(asignacion):
    # Si todas las regiones están asignadas
    if len(asignacion) == len(mapa):
        return asignacion if es_consistente(asignacion) else None

    # Seleccionar región no asignada
    region = next(r for r in mapa if r not in asignacion)

    for color in colores:
        nueva_asignacion = asignacion.copy()
        nueva_asignacion[region] = color
        if es_consistente(nueva_asignacion):
            resultado = backtracking(nueva_asignacion)
            if resultado:
                return resultado
    return None

def acondicionamiento(cutset):
    # Probar todas las combinaciones de colores para el cutset
    for combinacion in itertools.product(colores, repeat=len(cutset)):
        asignacion = dict(zip(cutset, combinacion))

        if not es_consistente(asignacion):
            continue

        # Resolver el resto con backtracking
        resultado = backtracking(asignacion)
        if resultado:
            return resultado
    return None

# Ejecución: elegir un cutset (por ejemplo, regiones A y B)
cutset = ["A", "B"]
solucion = acondicionamiento(cutset)

# Mostrar resultado
if solucion:
    print("Solución encontrada con Acondicionamiento del Corte:")
    for region, color in solucion.items():
        print(f"Región {region} → {color}")
else:
    print("No se encontró solución válida.")
