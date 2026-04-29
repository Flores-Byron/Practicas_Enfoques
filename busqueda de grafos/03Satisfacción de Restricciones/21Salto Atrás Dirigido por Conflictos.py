#definicion del mapa (grafo de regiones y sus vecinos)
mapa = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D"],
    "D": ["B", "C"]
}

# Colores disponibles
colores = ["Rojo", "Verde", "Azul"]

def es_consistente(asignacion, region, color):

    #verificar que ningun vecino tenga el mismo color
    for vecino in mapa[region]:
        if vecino in asignacion and asignacion[vecino] == color:
            return False
    return True

def salto_atras(regiones, asignacion={}, nivel=0):

    #si todas las regiones estan asignadas
    if nivel == len(regiones):
        return asignacion
    
    region = regiones[nivel]
    for color in colores:
        if es_consistente(asignacion, region, color):
            asignacion[region] = color
            resultado = salto_atras(regiones, asignacion.copy(), nivel+1)
            if resultado:
                return resultado
            else:
                #salto atras dirigido por conflicto:
                #si el color genera algun conflicto, retrocede directamente al nivel del vecino conflictivo
                for vecino in mapa[region]:
                    if vecino in asignacion and asignacion[vecino] == color:
                        return None  #se fuerza el salto atras
    return None

#ejecucion del algoritmo
regiones = list(mapa.keys())
solucion = salto_atras(regiones)

#mostrar el resultado
if solucion:
    print("Solución encontrada con Salto Atrás Dirigido por Conflictos:")
    for region, color in solucion.items():
        print(f"Región {region} → {color}")
else:
    print("No se encontró solución válida.")