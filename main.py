import random
import random as r



def mostrarTablero(tablero):
    for fila in tablero:
        print("|", end="")
        for numero in fila:
            print(numero, end="|")
        print("")

def crearTablero():
    tamañoCorrecto =  False
    while (not tamañoCorrecto):
        n = int(input("Que tamaño de tablero quieres?"))
        if(n>= 6 ):
            tablero=[[0 for i in range (n)]for i in range (n)]
            tamañoCorrecto=True
    return tablero


def colocarBarcosA(tablero):

    barcos=[4,3,2,2,1,1]

    while(barcos):
        direcion=r.choice(["v","h"])
        barco = barcos[0]
        fila = r.randint(0,len(tablero)-1)
        columna = r.randint(0,len(tablero)-1)
        if direcion == "h":
            if columna + barco <= len(tablero[0]):
                cabe=True

                for i in range(barco):
                    if tablero[fila][columna + i]!=0:
                        cabe=False
                if cabe:
                    for i in range (barco):
                        tablero[fila][columna+i]=barco
                    barcos.pop(0)


        elif direcion == "v":
            if fila + barco <= len(tablero):
                cabe = True

                for i in range(barco):
                    if tablero[fila+i][columna ] != 0:
                        cabe = False
                if cabe:
                    for i in range(barco):
                        tablero[fila+i][columna] = barco
                    barcos.pop(0)

    mostrarTablero(tablero)



tablero=crearTablero()
colocarBarcosA(tablero)