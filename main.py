import sys
import random
from io import open

# Practica realizada por Juan Antonio Pages Lopez y Fernando San Jose Dominguez
# Coding: UTF8

class Celda:                                                # Creamos el objeto celda

    '''Inicialiazmos las propiedades del objeto celda'''

    def __init__(self):

        self.__valor = " "
        self.__modo = 1
        self.__modoValor = " "
        self.__lock = False

    '''Obtenemos la propiedad lock del objeto'''

    def getLock(self):

        return self.__lock

    '''Fijamos la propiedad lock'''

    def setLock(self, lock):

        self.__lock = lock

    '''Obtenemos la propiedad valor del objeto'''

    def getValor(self):

        return self.__valor

    '''Fijamos la propiedad'''

    def setValor(self, valor):

        self.__valor = valor

    '''Fijamos el modo que esta seleccionado'''

    def setMode(self, modo):

        self.__modo = modo

    '''Cambiamos al modo que queramos'''

    def getModeValor(self):

        dic1 = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H", 9: "I", 10: "J", 11: "K"}

        if self.__modo == 1:
            if self.__valor == "*":
                self.__modoValor = "*"                          # Obstaculos para modo 1
            elif self.__valor == " ":
                self.__modoValor = " "                          # Celdas vacias para modo 1
            else:
                self.__modoValor = dic1[self.__valor]           # Bloques para modo 1
            return self.__modoValor

        dic2 = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: 11}

        if self.__modo == 2:
            if self.__valor == "*":
                self.__modoValor = "**"                         # Obstaculos para modo 2
            elif self.__valor == " ":
                self.__modoValor = " "                          # Celdas vacias para modo 2
            else:
                self.__modoValor = dic2[self.__valor]           # Bloques para modo 2
            return self.__modoValor

        dic3 = {1: 1, 2: 2, 3: 4, 4: 8, 5: 16, 6: 32, 7: 64, 8: 128, 9: 256, 10: 512, 11: 1024}

        if self.__modo == 3:
            if self.__valor == "*":
                self.__modoValor = "****"                       # Obstaculos para modo 3
            elif self.__valor == " ":
                self.__modoValor = " "                          # Celdas vacias para modo 3
            else:
                self.__modoValor = dic3[self.__valor]           # Bloques para modo 3
            return self.__modoValor

        dic4 = {1: 2, 2: 4, 3: 8, 4: 16, 5: 32, 6: 64, 7: 128, 8: 256, 9: 512, 10: 1024, 11: 2048}

        if self.__modo == 4:
            if self.__valor == "*":
                self.__modoValor = "****"                       # Obstaculos para modo 4
            elif self.__valor == " ":
                self.__modoValor = " "                          # Celdas vacias para modo 4
            else:
                self.__modoValor = dic4[self.__valor]           # Bloques para modo 4
            return self.__modoValor


'''Te envia al menu principal'''


def menu():

    print("--------------------  CLON-3  --------------------\n- Practica de Paradigmas de Programacion 2019-20 ",
          end="")
    print("-\n--------------------------------------------------")
    print("\n1. CREAR NUEVO TABLERO\n2. LEER TABLERO DE FICHERO\n3. SALIR")

    select = int(input("\nSelecione una opcion: "))
    if select == 3:                                 # Si el usuario selecciona 3
        sys.exit(0)                                 # Finaliza el programa

    return select


'''Imprime en consola el tablero vacio'''


def imprimirTab(tam, modo, celdas):
    if modo == 3:                       # Para conseguir imprimir los 4 huecos vacios en modo 3
        modo = 4

    for i in range(tam):
        print("+", end="")
        for j in range(tam):
            for k in range(modo):
                print("-", end="")
            print("+", end="")
        print("")
        for l in range(tam):
            print("|", end="")
            for k in range(modo - len(str(celdas[l][i].getModeValor()))):
                print(" ", end="")
            print(celdas[l][i].getModeValor(), end="")
        print("|")
    print("+", end="")
    for j in range(tam):
        for k in range(modo):
            print("-", end="")
        print("+", end="")


'''Guarda el tablero en un archivo .tab'''


def save(tam, celdas):
    fichero = input("Nombre del fichero: ")
    f = open(fichero, "w")                                  # Crea y abre el archivo en modo escritura
    f.write(str(moves) + "\n" + str(score))                 # Copia los movimientos y la puntuación

    for i in range(tam):                                    # Recorre las celdas en eje y
        f.write("\n")
        for j in range(tam):                                # Recorre las celdas en eje x
            celdas[j][i].setMode(1)                         # Cambia el modo al 1(Alfabetico)
            if celdas[j][i].getValor() == " ":
                f.write(".")                                # Transforma los espacios en puntos
            else:
                f.write(str(celdas[j][i].getModeValor()))   # Escribe el caracter que haya en cada celda

    f.close()                                               # Cierra el flujo de datos


'''Carga el tablero de un archivo .tab'''


def load():

    fichero = input("Nombre del fichero: ")                         # Pide el nombre del fichero
    f = open(fichero, "r")                                          # Abre el fichero en modo lectura
    moves = f.readline()                                            # Lee los movimientos del fichero
    score = f.readline()                                            # Lee la puntuación del fichero
    tam = len(f.readline()) - 1                                     # Lee el tamaño del tablero
    celdas = [[Celda() for i in range(tam)] for j in range(tam)]    # Crea la lista celdas
    historial = [celdas]
    scorejugada = 0
    f.seek(len(moves)+len(score)+2)                                 # Coloca el puntero en el tablero
    dic = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11}

    for i in range(tam):                                            # Recorre las filas
        linea = f.readline()                                        # Lee las filas del tablero
        for j in range(tam):                                        # Recorre las columnas
            if linea[j] == ".":                                     # Comprueba si hay espacios
                celdas[j][i].setValor(" ")
            elif linea[j] == "\n":                                  # Si hay salto de linea salta a la siguiente fila
                break
            elif linea[j] == "*":                                   # Comprueba si hay obstaculo
                celdas[j][i].setValor("*")
            else:
                celdas[j][i].setValor(dic[linea[j]])                # Coloca el bloque que haya en el fichero

    f.close()                                                       # Cerramos el flujo de datos
    return celdas, int(moves), int(score), int(tam), historial, scorejugada


'''Añade un bloque nuevo de distinto nivel(1 o 2) cada vez que hay movimiento'''


def addCelda(tam, celdas, historial):

    prob = random.choices([1, 2], [0.75, 0.25])             # Probabilidad del 75% de nivel 1 y 25% de nivel 2
    historial.append(celdas)

    while True:
        randIntX = randInt(tam)                             # Genera una coordenada x random
        randIntY = randInt(tam)                             # Genera una coordenada y random

        if celdas[randIntX][randIntY].getValor() == " ":    # Genera la celda donde haya un hueco libre
            celdas[randIntX][randIntY].setValor(prob[0])
            break

    for i in range(tam):
        for j in range(tam):
            celdas[j][i].setLock(False)

    return celdas, historial


'''Genera un int random generico'''


def randInt(max):

    rand = int(random.random() * max)
    return rand


'''Comprueba si la partida a finalizado'''


def fin(tam, celdas):
    maximo = tam * tam                          # Numero maximo de celdas
    contmax = 0

    for i in range(tam):
        for j in range(tam):
            if celdas[j][i].getValor() != " ":  # Comprueba si todas las celdas están llenas
                contmax += 1

    if contmax == maximo:                       # Si las celdas estan llenas la partida finaliza
        imprimirTab(tam, modo, celdas)          # Imprime el tablero lleno
        print("\n\n---  FIN DEL JUEGO ---\n")
        menu()                                  # Vuelve al menu principal


'''Inicializamos las celdas del tablero'''


def initCelda(tam, obs):

    celdas = [[Celda() for i in range(tam)] for j in range(tam)]    # Crea la lista celdas
    historial = [celdas]
    cont = 0
    for i in range(obs):                                            # Creamos los obstaculos

        while cont <= i:
            randIntX = randInt(tam)                                 # Genera una coordenada x random
            randIntY = randInt(tam)                                 # Genera una coordenada y random

            if celdas[randIntX][randIntY].getValor() == " ":        # Genera obstaculo si la celda esta vacia
                celdas[randIntX][randIntY].setValor("*")
                cont += 1

    for i in range(2):                                              # Genera dos bloques random en celdas vacias
        addCelda(tam, celdas, historial)

    return celdas, historial


'''Mueve hacia la derecha'''


def derecha(tam, celdas, score):

    scorejugada = 0

    print("\n--- DERECHA ---")

    for k in range(tam):
        for i in range(tam):
            for j in range(tam - 1, 0, -1):
                if celdas[j][i].getValor() == " ":                          # Comprueba si es espacio
                    if celdas[j - 1][i].getValor() != "*":                  # Comprueba si no es obstaculo
                        celdas[j][i].setValor(celdas[j - 1][i].getValor())  # Mueve lo que hay en tam-1 a tam
                        celdas[j - 1][i].setValor(" ")                      # Borra el valor anterior
                elif celdas[j][i].getValor() == celdas[j - 1][i].getValor() and celdas[j][i].getValor() != "*":
                    if not celdas[j-1][i].getLock():
                        celdas[j][i].setValor(celdas[j][i].getValor() + 1)  # Fusiona dos celdas del mismo nivel
                        celdas[j - 1][i].setValor(" ")                      # Borra el valor anterior
                        celdas[j][i].setLock(True)                          # Actualiza el bloqueo
                        score += 1                                          # Suma uno cada vez que fusiona
                        scorejugada += 1

    return celdas, score, scorejugada


'''Mueve a la izquierda'''


def izquierda(tam, celdas, score):

    scorejugada = 0

    print("\n--- IZQUIERDA ---")
    for k in range(tam):
        for i in range(tam):
            for j in range(0, tam - 1, 1):
                if celdas[j][i].getValor() == " ":                          # Comprueba si es espacio
                    if celdas[j + 1][i].getValor() != "*":                  # Comprueba si no es obstaculo
                        celdas[j][i].setValor(celdas[j + 1][i].getValor())  # Mueve lo que hay en tam-1 a tam
                        celdas[j + 1][i].setValor(" ")                      # Borra el valor anterior
                elif celdas[j][i].getValor() == celdas[j + 1][i].getValor() and celdas[j][i].getValor() != "*":
                    if not celdas[j + 1][i].getLock():                      # Comprueba si esta bloqueada
                        celdas[j][i].setValor(celdas[j][i].getValor() + 1)  # Fusiona dos celdas del mismo nivel
                        celdas[j + 1][i].setValor(" ")                      # Borra el valor anterior
                        celdas[j][i].setLock(True)                          # Actualiza el bloqueo
                        score += 1                                          # Suma uno cada vez que fusiona
                        scorejugada += 1

    return celdas, score, scorejugada


'''Mueve hacia arriba'''


def subir(tam, celdas, score):

    scorejugada = 0

    print("\n--- SUBIR ---")
    for k in range(tam):
        for i in range(0, tam - 1, 1):
            for j in range(tam):
                if celdas[j][i].getValor() == " ":                          # Comprueba si es espacio
                    if celdas[j][i + 1].getValor() != "*":                  # Comprueba si no es obstaculo
                        celdas[j][i].setValor(celdas[j][i + 1].getValor())  # Mueve lo que hay en tam-1 a tam
                        celdas[j][i + 1].setValor(" ")                      # Borra el valor anterior
                elif celdas[j][i].getValor() == celdas[j][i + 1].getValor() and celdas[j][i].getValor() != "*":
                    if not celdas[j][i + 1].getLock():                      # Comprueba si esta bloqueada
                        celdas[j][i].setValor(celdas[j][i].getValor() + 1)  # Fusiona dos celdas del mismo nivel
                        celdas[j][i + 1].setValor(" ")                      # Borra el valor anterior
                        celdas[j][i].setLock(True)                          # Actualiza el bloqueo
                        score += 1                                          # Suma uno cada vez que fusiona
                        scorejugada += 1

    return celdas, score, scorejugada


'''Mueve hacia abajo'''


def bajar(tam, celdas, score):

    scorejugada = 0

    print("\n--- BAJAR ---")
    for k in range(tam):
        for i in range(tam - 1, 0, -1):
            for j in range(tam):
                if celdas[j][i].getValor() == " ":                          # Comprueba si es espacio
                    if celdas[j][i - 1].getValor() != "*":                  # Comprueba si no es obstaculo
                        celdas[j][i].setValor(celdas[j][i - 1].getValor())  # Mueve lo que hay en tam-1 a tam
                        celdas[j][i - 1].setValor(" ")
                elif celdas[j][i].getValor() == celdas[j][i - 1].getValor() and celdas[j][i].getValor() != "*":
                    if not celdas[j][i - 1].getLock():                      # Comprueba si esta bloqueada
                        celdas[j][i].setValor(celdas[j][i].getValor() + 1)  # Fusiona dos celdas del mismo nivel
                        celdas[j][i - 1].setValor(" ")
                        celdas[j][i].setLock(True)                          # Actualiza el bloqueo
                        score += 1                                          # Suma uno cada vez que fusiona
                        scorejugada += 1

    return celdas, score, scorejugada


'''Vuelve hacia atras'''

def atras(score, moves, historial, scorejugada):

    historial.pop(moves)                        # Quita el ultimo elemento de historial
    celdas = historial[moves-1]                 # Iguala celdas a la lista de listas anterior

    if moves > 0:
        moves -= 1
    else:
        moves = 0

    if score > 0:
        score -= scorejugada
    else:
        score = 0

    return celdas, score, moves, historial


'''Entra en el bucle del juego'''

def play(tam, celdas, moves, score, modo, historial):

    while True:                                                         # Acaba si el usuario pulsa [F]in o [G]uardar

        fin(tam, celdas)                                                # Comprueba la partida ha finalizado
        imprimirTab(tam, modo, celdas)                                  # Imprime el tablero

        print("\n\nMOVIMIENTOS:", moves, "| PUNTUACIÓN:", score)
        letra = input("[S]ubir, [B]ajar, [I]zda, [D]cha, [A]tras | [M]odo, [G]uardar, [F]in: \n")
        if letra == "M":                                                # Enseña los modos a los que cambiar
            print("\nMODOS DE VISUALIZACIÓN: \n")
            print("1.Alfabético\n2.Numérico\n3.1024\n4.2048")

            modo = int(input("\nEscoja modo: "))                        # Pide el modo al usuario

            for i in range(tam):
                for j in range(tam):
                    celdas[j][i].setMode(modo)                          # Actualiza el modo de todas las celdas

        elif letra == "G":                                              # Guarda la partida
            save(tam, celdas)                                           # Genera un fichero con la partida
            return

        elif letra == "F":                                              # Vuelve al menu del principal del juego
            return

        elif letra == "S":                                              # Mueve hacia arriba
            moves += 1                                                  # Suma 1 a los movimientos
            celdas, score, scorejugada = subir(tam, celdas, score)      # Actualiza el tablero
            addCelda(tam, celdas, historial)                            # Añade una celda random

        elif letra == "B":                                              # Mueve hacia abajo
            moves += 1                                                  # Suma 1 a los movimientos
            celdas, score, scorejugada = bajar(tam, celdas, score)      # Actualiza el tablero
            addCelda(tam, celdas, historial)                            # Añade una celda random

        elif letra == "I":                                              # Mueve hacia la izquierda
            moves += 1                                                  # Suma 1 a los movimientos
            celdas, score, scorejugada = izquierda(tam, celdas, score)  # Actualiza el tablero
            addCelda(tam, celdas, historial)                            # Añade una celda random

        elif letra == "D":                                              # Mueve hacia la derecha
            moves += 1                                                  # Suma 1 a los movimientos
            celdas, score, scorejugada = derecha(tam, celdas, score)    # Actualiza el tablero
            addCelda(tam, celdas, historial)                            # Añade una celda random

        elif letra == "A":
            celdas, score, moves, historial = atras(score, moves, historial, scorejugada)


while True:                                                     # Bucle principal del juego

    opcion = menu()                                             # Llamo a menu() porque necesito la variable select
    if opcion == 1:                                             # Si selecciona opcion 1
        modo = 1
        tam = int(input("Tamaño del tablero: "))                # Pide dimensiones del tablero
        obs = int(input("Numero de obstaculos: "))              # Pide el numero de obstaculos
        celdas, historial = initCelda(tam, obs)                 # Inicializa el tablero
        moves = 0                                               # Inicializa el movimientos
        score = 0                                               # Inicializa la puntacion
        play(tam, celdas, moves, score, modo, historial)

    elif opcion == 2:                                           # Carga una partida guardada
        celdas, moves, score, tam, historial, scorejugada = load()
        modo = 1
        play(tam, celdas, moves, score, modo, historial)        # Comienza a jugar
