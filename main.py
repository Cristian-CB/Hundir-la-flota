import random as r

def barcoHundido(tableroE,barco):

        esta = False


        for fila in tableroE:
            for casilla in fila:
                if casilla == barco:
                    esta = True

        if not esta:
            print(f"Barco {barco} hundido")














def mostrarTablero(tablero):
    print("    ", end=" ")
    for numero in range(len(tablero[0])):
        print(numero, end="  ")
    print()

    contador = 0

    for fila in tablero:
        print(contador, end="  |")
        for numero in fila:
            print(numero, end="|")
        print()
        contador += 1


def crearTablero():
    tamañoCorrecto = False
    while not tamañoCorrecto:
        n = int(input("Que tamaño de tablero quieres?"))
        if n >= 6:
            tablero = [["🌊" for i in range(n)] for i in range(n)]
            tamañoCorrecto = True
    return tablero, n


def crearTableroEnemigo(n):
    tableroE = [["🌊" for i in range(n)] for i in range(n)]
    return tableroE


barcos = [4, 3, 2, 2, 1, 1]
barcose = [4, 3, 2, 2, 1, 1]

pixelBarcos = ["⛵","🚤","🛥️","️⛴️","🚢","🛳️"]
pixelBarcos1 = pixelBarcos.copy()
pixelBarcos2 = pixelBarcos.copy()


def colocarBarcosA(tablero, barcos, pixelBarcos):
    while barcos:
        direcion = r.choice(["v", "h"])
        barco = barcos[0]
        fila = r.randint(0, len(tablero) - 1)
        columna = r.randint(0, len(tablero) - 1)

        if direcion == "h":
            if columna + barco <= len(tablero[0]):
                cabe = True

                for i in range(barco):
                    if tablero[fila][columna + i] != "🌊":
                        cabe = False

                if cabe:
                    for i in range(barco):
                        tablero[fila][columna + i] = pixelBarcos[0]

                    barcos.pop(0)
                    pixelBarcos.pop(0)

        elif direcion == "v":
            if fila + barco <= len(tablero):
                cabe = True

                for i in range(barco):
                    if tablero[fila + i][columna] != "🌊":
                        cabe = False

                if cabe:
                    for i in range(barco):
                        tablero[fila + i][columna] = pixelBarcos[0]

                    barcos.pop(0)
                    pixelBarcos.pop(0)


def atacar(tableroE, tableroVisible, pixelBarcos1):
    columnaYFilaCorrectos = False

    while not columnaYFilaCorrectos:
        columna = int(input("¿Qué columna? "))
        fila = int(input("¿Qué fila? "))

        if 0 <= columna < len(tableroE[0]) and 0 <= fila < len(tableroE):
            if tableroVisible[fila][columna] == "🌊":
                columnaYFilaCorrectos = True
            else:
                print("Ya has atacado esa casilla")
        else:
            print("Introduce filas y columnas existentes")

    if tableroE[fila][columna] in pixelBarcos1:
        print("¡Le has dado!")
        barco = tableroE[fila][columna]
        tableroVisible[fila][columna] = "💥"
        tableroE [fila][columna] = "💥"
        barcoHundido(tableroE,barco)
        return True
    else:
        print("Agua")
        tableroVisible[fila][columna] = "💨"
        return False


def atacarIa(tablero, pixelBarcos1):
    while True:
        columna = r.randint(0, len(tablero[0]) - 1)
        fila = r.randint(0, len(tablero) - 1)

        if tablero[fila][columna] in pixelBarcos1:
            tablero[fila][columna] = "💥"
            recordar = True
            return True, fila, columna, recordar

        elif tablero[fila][columna] == "🌊":
            tablero[fila][columna] = "💨"
            recordar = False
            return False, fila, columna, recordar


def ataqueIa(tablero, fila, columna, barcosRestantesE, pixelBarcos1):
    recordar = True

    if barcosRestantesE < 12 and r.choice([0, 1, 1]):

        while True:
            columna = r.randint(0, len(tablero[0]) - 1)
            fila = r.randint(0, len(tablero) - 1)

            if tablero[fila][columna] in pixelBarcos1:
                tablero[fila][columna] = "💥"
                recordar = True
                return True, fila, columna, recordar


    else:



        intentos = 0
        while intentos < 4:
            direccion = r.choice([0, 1])
            nuevaFila = fila
            nuevaColumna = columna

            if direccion == 0:
                cambioFila = r.choice([1, -1])
                nuevaFila = fila + cambioFila
            else:
                cambioColumna = r.choice([1, -1])
                nuevaColumna = columna + cambioColumna

            intentos += 1

            if (0 <= nuevaFila < len(tablero)
                    and 0 <= nuevaColumna < len(tablero[0])):

                if (tablero[nuevaFila][nuevaColumna] != "💨"
                        and tablero[nuevaFila][nuevaColumna] != "💥"):

                    if tablero[nuevaFila][nuevaColumna] in pixelBarcos1:
                        tablero[nuevaFila][nuevaColumna] = "💥"
                        return True, nuevaFila, nuevaColumna, recordar

                    elif tablero[nuevaFila][nuevaColumna] == "🌊":
                        tablero[nuevaFila][nuevaColumna] = "💨"
                        recordar = False
                        return False, nuevaFila, nuevaColumna, recordar

    acierto, fila, columna, recordar = atacarIa(tablero, pixelBarcos1)
    return acierto, fila, columna, recordar


tablero, n = crearTablero()
tableroE = crearTableroEnemigo(n)
tableroVisible = crearTableroEnemigo(n)

colocarBarcosA(tablero, barcos.copy(), pixelBarcos.copy())
colocarBarcosA(tableroE, barcose.copy(), pixelBarcos.copy())

barcosRestantesE = sum(barcose)
barcosRestantes = sum(barcos)

mostrarTablero(tableroVisible)
print("         Tu tablero")
print("-----------------------------")
mostrarTablero(tablero)

recordar = False
fila = 0
columna = 0

while barcosRestantes > 0 and barcosRestantesE > 0:

    if atacar(tableroE, tableroVisible, pixelBarcos2):
        barcosRestantesE -= 1
        print("Barcos restantes del enemigo:", barcosRestantesE)

    mostrarTablero(tableroVisible)



    if recordar:
        acierto, fila, columna, recordar = ataqueIa(tablero, fila, columna, barcosRestantes, pixelBarcos1)
    else:
        acierto, fila, columna, recordar = atacarIa(tablero, pixelBarcos1)

    if acierto:
        barcosRestantes -= 1
        print("Tus casillas de barco restantes:", barcosRestantes)

    print("Tu tablero")
    print("-------------------------------")
    mostrarTablero(tablero)
if( barcosRestantes == 0):
    print("La ia te ha ganado")
    mostrarTablero(tableroE)
else:
    print("has ganado!")