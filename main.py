from turtledemo.penrose import start


def crearTablero():
    tamañoCorrecto =  False
    while (not tamañoCorrecto):
        n = int(input("Que tamaño de tablero quieres?"))
        if(n>= 6 ):
            tablero=[[0 for i in range (n)]for i in range (3)]


            print(tablero)
            for fila in tablero:
                print("|",end="")
                for numero in fila:
                    print(numero, end="|")
                print("")




        tamañoCorrecto=True







crearTablero()