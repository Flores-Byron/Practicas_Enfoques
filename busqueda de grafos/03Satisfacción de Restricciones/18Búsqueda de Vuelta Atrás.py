def es_valido(tablero, fila, columna):

    #verificar columna
    for i in range(fila):
        if tablero[i] == columna:
            return False
    
    #verificar diagonales
    for i in range(fila):
        if abs(tablero[i] - columna) == abs(i - fila):
            return False
    
    return True

def busqueda_reinas(n, fila=0, tablero=None):
    if tablero is None:
        tablero = [-1] * n

    if fila == n:
        return tablero #encontramos una solucion
    
    for columna in range(n):
        if es_valido(tablero, fila, columna):
            tablero[fila] = columna
            resultado = busqueda_reinas(n, fila+1, tablero)
            if resultado:
             return resultado
            tablero[fila] = -1 #retroceder una busqueda

    return None

#ejemplo de uso: 4 reinas
solucion = busqueda_reinas(4)
print("solucion encontrada (columna por fila):", solucion)