import random
import random as r



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
    tamañoCorrecto =  False
    while (not tamañoCorrecto):
        n = int(input("Que tamaño de tablero quieres?"))
        if(n>= 6 ):
            tablero=[["🌊" for i in range (n)]for i in range (n)]
            tamañoCorrecto=True
    return tablero , n


def crearTableroEnemigo(n):
            tableroE=[["🌊" for i in range (n)]for i in range (n)]
            return tableroE


barcos=[4,3,2,2,1,1]
barcose=[4,3,2,2,1,1]

def colocarBarcosA(tablero , barcos):
    while(barcos):
        direcion=r.choice(["v","h"])
        barco = barcos[0]
        fila = r.randint(0,len(tablero)-1)
        columna = r.randint(0,len(tablero)-1)
        if direcion == "h":
            if columna + barco <= len(tablero[0]):
                cabe=True

                for i in range(barco):
                    if tablero[fila][columna + i]!="🌊":
                        cabe=False
                if cabe:
                    for i in range (barco):
                        tablero[fila][columna+i]="🚢"
                    barcos.pop(0)


        elif direcion == "v":
            if fila + barco <= len(tablero):
                cabe = True

                for i in range(barco):
                    if tablero[fila+i][columna ] != "🌊":
                        cabe = False
                if cabe:
                    for i in range(barco):
                        tablero[fila+i][columna] = "🚢"
                    barcos.pop(0)







def atacar(tableroE, tableroVisible):
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

    if tableroE[fila][columna] == "🚢":
        print("¡Le has dado!")
        tableroVisible[fila][columna] = "💥"
        return True
    else:
        print("Agua")
        tableroVisible[fila][columna] = "💨"
        return False

def atacarIa(tablero):
    acierto = False


    if(x<5):
        while not acierto:
            columna = r.randint(0,len(tablero)-1)
            fila = r.randint(0,len(tablero)-1)
            if(tablero[fila][columna]== "🚢"):
                tablero[fila][columna] = "💥"
                return True

    else:


        while not acierto:
            columna = r.randint(0,len(tablero)-1)
            fila = r.randint(0,len(tablero)-1)
            if(tablero[fila][columna]== "🚢"):
                tablero[fila][columna] = "💥"
                return True
            elif (tablero[fila][columna]== "🌊"):
                tablero[fila][columna] = "💨"
                return False








jugadores=["x","y"]

tablero,n=crearTablero()
tableroE=crearTableroEnemigo(n)
tableroVisible = crearTableroEnemigo(n)

colocarBarcosA(tablero,barcos.copy())
colocarBarcosA(tableroE,barcose.copy())




barcosRestantesE = sum(barcose)
barcosRestantes = sum(barcos)
mostrarTablero(tableroVisible)
print("         Tu tablero")
print("-----------------------------")
mostrarTablero(tablero)

while barcosRestantes > 0 and  barcosRestantesE > 0  :
    if atacar(tableroE, tableroVisible):
        barcosRestantesE -= 1
        print("Casillas de barco restantes:", barcosRestantes)

    mostrarTablero(tableroVisible)
    if atacarIa(tablero):
        barcosRestantes -= 1
        print("holaaa")
    print("           Tu tablero")
    print("-------------------------------")
    mostrarTablero(tablero)

if(barcosRestantesE==0):
    print("Felicidades has ganado")
else:
    print("has perdido")




print("¡Has ganado! Has hundido todos los barcos.")