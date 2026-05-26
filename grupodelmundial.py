# Cristian Beltran
# Parcial Logica de Programacion
# 26 de Mayo de 2026
# Simulador de Grupo K del Mundial 2026

# Grupo K del Mundial 2026
grupo_k = [
    "Portugal",
    "RD Congo",
    "Uzbekistán",
    "Colombia"
]

# Crear tabla de puntos
tabla = {}

for equipo in grupo_k:
    tabla[equipo] = {
        "puntos": 0,
        "gf": 0,   # goles a favor
        "gc": 0,   # goles en contra
        "dg": 0    # diferencia de gol
    }


print("   GRUPO K - MUNDIAL 2026")


# Partidos oficiales del grupo
partidos = [
    ("Portugal", "RD Congo"),
    ("Uzbekistán", "Colombia"),
    ("Portugal", "Uzbekistán"),
    ("Colombia", "RD Congo"),
    ("Colombia", "Portugal"),
    ("RD Congo", "Uzbekistán")
]

# Registrar resultados
for local, visitante in partidos:

    print(f"\n{local} vs {visitante}")

    goles_local = int(input(f"Goles de {local}: "))
    goles_visitante = int(input(f"Goles de {visitante}: "))

    # Actualizar goles
    tabla[local]["gf"] += goles_local
    tabla[local]["gc"] += goles_visitante

    tabla[visitante]["gf"] += goles_visitante
    tabla[visitante]["gc"] += goles_local

    # Resultado
    if goles_local > goles_visitante:
        tabla[local]["puntos"] += 3

    elif goles_visitante > goles_local:
        tabla[visitante]["puntos"] += 3

    else:
        tabla[local]["puntos"] += 1
        tabla[visitante]["puntos"] += 1

# Calcular diferencia de gol
for equipo in tabla:
    tabla[equipo]["dg"] = (
        tabla[equipo]["gf"] - tabla[equipo]["gc"]
    )

# Ordenar tabla
posiciones = sorted(
    tabla.items(),
    key=lambda x: (x[1]["puntos"], x[1]["dg"], x[1]["gf"]),
    reverse=True
)

# Mostrar tabla
print(" TABLA DE POSICIONES")

print(f"{'Equipo':15} {'PTS':5} {'GF':5} {'GC':5} {'DG':5}")

for equipo, datos in posiciones:
    print(
        f"{equipo:15} "
        f"{datos['puntos']:5} "
        f"{datos['gf']:5} "
        f"{datos['gc']:5} "
        f"{datos['dg']:5}"
    )
