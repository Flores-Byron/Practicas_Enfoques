# Definición del mapa (grafo de regiones y sus vecinos)
mapa = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D"],
    "D": ["B", "C"]
}

# Colores disponibles
colores = ["Rojo", "Verde", "Azul"]

def propagar(asignacion, dominios, region, color):
    # Asignar color a la región
    asignacion[region] = color
    dominios[region] = [color]

    # Propagar restricciones a los vecinos
    for vecino in mapa[region]:
        if color in dominios[vecino]:
            dominios[vecino].remove(color)
            # Si un vecino se queda con un solo color, propagar automáticamente
            if len(dominios[vecino]) == 1 and vecino not in asignacion:
                nuevo_color = dominios[vecino][0]
                if not propagar(asignacion, dominios, vecino, nuevo_color):
                    return False
            # Si un vecino se queda sin colores, fallo
            if not dominios[vecino]:
                return False
    return True

def backtracking_cp(asignacion, dominios):
    # Si todas las regiones están asignadas
    if all(len(dominios[region]) == 1 for region in mapa):
        return asignacion

    # Seleccionar región no asignada
    region = next(r for r in mapa if len(dominios[r]) > 1)

    for color in dominios[region][:]:
        nueva_asignacion = asignacion.copy()
        nuevos_dominios = {r: dominios[r][:] for r in dominios}

        if propagar(nueva_asignacion, nuevos_dominios, region, color):
            resultado = backtracking_cp(nueva_asignacion, nuevos_dominios)
            if resultado:
                return resultado
    return None

# Ejecución del algoritmo
asignacion_inicial = {}
dominios_iniciales = {region: colores[:] for region in mapa}
solucion = backtracking_cp(asignacion_inicial, dominios_iniciales)

# Mostrar resultado
if solucion:
    print("Solución encontrada con Propagación de Restricciones:")
    for region, color in solucion.items():
        print(f"Región {region} → {color}")
else:
    print("No se encontró solución válida.")
