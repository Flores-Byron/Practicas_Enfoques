# Estrategias: "confesar" o "silencio"
estrategias = ["confesar", "silencio"]

# Matriz de pagos (jugador A, jugador B)
# Valores negativos = años de cárcel
pagos = {
    ("confesar", "confesar"): (-5, -5),
    ("confesar", "silencio"): (0, -10),
    ("silencio", "confesar"): (-10, 0),
    ("silencio", "silencio"): (-1, -1)
}

def mejor_respuesta(estrategia_oponente):
    # Jugador A evalúa sus opciones
    opciones = {a: pagos[(a, estrategia_oponente)][0] for a in estrategias}
    return max(opciones, key=opciones.get)

# Evaluar equilibrio de Nash
for a in estrategias:
    for b in estrategias:
        pagoA, pagoB = pagos[(a,b)]
        if a == mejor_respuesta(b) and b == mejor_respuesta(a):
            print(f"Equilibrio de Nash: ({a}, {b}) → pagos {pagoA}, {pagoB}")
