#definicion de mapa (grafo de regiones y sus vecinos)
mapa = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D"],
    "D": ["B", "C"]
}

#colores disponibles
colores = ["Rojo", "Verde", "Azul"]

def comprobacion(asignacion, dominios, region, color):
    #asiganacion de color a la region
    asignacion[region] = color
    dominios[region] = [color]

    #eliminar color de los vecinos
    for vecinos in mapa[region]:
        if color in dominios[vecinos]:
            dominios[vecinos].remove(color)
            #si un vecino se queda sin color, fallo
            if not dominios[vecinos]:
                return False
    return True

def comprobacion_fc(asignacion, dominios):
    #si todas las regiones estan asignadas
    if all(len(dominios[region]) == 1 for region in mapa):
        return asignacion
    
    #seleccionar region no asignada
    region = next(r for r in mapa if len(dominios[r]) > 1)

    for color in dominios[region][:]:
        #copiar dominios y asignaciones
        nueva_asignacion = asignacion.copy()
        nuevos_dominios = {r: dominios[r][:] for r in dominios}

        if comprobacion(nueva_asignacion, nuevos_dominios, region, color):
            resultado = comprobacion_fc(nueva_asignacion, nuevos_dominios)
            if resultado:
                return resultado
    return None

#ejecucion del algoritmo
asignacion_inicial = {}
dominios_iniciales = {region: colores[:] for region in mapa}
solucion = comprobacion_fc(asignacion_inicial, dominios_iniciales)
print("Solución encontrada con Forward Checking:", solucion)