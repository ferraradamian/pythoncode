# Reversi

import random
import sys

def dibujarTablero(tablero):
    # Esta funcion dibuja el tablero recibido. Devuelve None. 
    LÍNEAH = '  +---+---+---+---+---+---+---+---+' 
    LÍNEAV = '  |   |   |   |   |   |   |   |   |' 
 
    print('    1   2   3   4   5   6   7   8') 
    print(LÍNEAH)
    for y in range(8):
        print(LÍNEAV) 
        print(y+1, end=' ') 
        for x in range(8): 
            print('| %s' % (reiniciarTablero[x][y]), end=' ') 
        print('|') 
        print(LÍNEAV) 
        print(LÍNEAH)


def reiniciarTablero(tablero):
    # Deja en blanco el tablero recibido como argumento, excepto la posición inicial.
    for x in range(8):
        for y in range(8):
            tablero[x][y] = ' '

    # Piezas iniciales:
    tablero[3][3] = 'X' 
    tablero[3][4] = 'O' 
    tablero[4][3] = 'O' 
    tablero[4][4] = 'X'


def obtenerNuevoTablero():     
    # Crea un tablero nuevo, vacío. 
    tablero= [] 
    for i in range(8):
        tablero.append([' ' * 8])


    return tablero

def esJugadaValida(tablero, baldosa, comienzox, comienzoy):
    # Devuelve False si la jugada del jugador en comienzox, comienzoy es invalida 
    # Si es una jugada válida, devuelve una lista de espacios que pasarían a ser del jugador si moviera aquí.
    if tablero[comienzox][comienzoy] != ' ' or not estáEnTablero(comienzox, comienzoy): 
        return False

    tablero[comienzox][comienzoy] = baldosa # coloca temporariamente la baldosa sobre el tablero.    

    if baldosa == 'X': 
        otraBaldosa = 'O' 
    else: 
        otraBaldosa = 'X' 

    baldosasAConvertir = [] 
    for direccionx, direcciony in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]: 
        x, y = comienzox, comienzoy 
        x += direccionx # primer paso en la dirección 
        y += direcciony # primer paso en la dirección 
        if estaEnTablero(x, y) and tablero[x][y] == otraBaldosa: 
            # Hay una pieza perteneciente al otro jugador al lado de nustra pieza 
            x += direccionx  
            y += direcciony  
            if not estaEnTablero(x, y): 
                continue 
            while tablero[x][y] == otraBaldosa: 
                x += direccionx  
                y += direcciony  
                if not estaEnTablero(x, y): # sale del bucle while y continua en el bucle for. 
                    break 
            if not estaEnTablero(x, y): 
                continue 
            if tablero[x][y] == baldosa:  
                # Hay fichas a convertir. Caminar en dirección opuesta hasta llegar al casillero original, registrando todas las posiciones en el camino. 
                while True: 
                    x -= direccionx 
                    y -= direcciony 
                    if x == direccionxand y == direcciony: 
                        break 
                    baldosasAConvertir.append([x, y]) 
  
    tablero[comienzox][comienzoy] = ' ' # restablecer el espacio vacío 
    if len(baldosasAConvertir) == 0: # Si no se convirtió ninguna baldosa, la jugada no es válida. 
        return False 
    return baldosasAConvertir 
 
  
def estaEnTablero(x, y): 
    # Devuelve True si las coordenadas se encuentran dentro del tablero 
    return x >= 0 and x <= 7 and y >= 0 and y <= 7 
   
   
def obtenerTableroConJugadasValidas(tablero, baldosa): 
    # Devuelve un nuevo tablero, marcando con "." las jugadas válidas que el jugador puede realizar. 
    replicaTablero = obtenerCopiaTablero(tablero) 
  
    for x, y in obtenerJugadasValidas(replicaTablero, baldosa): 
        replicaTablero[x][y] = '.' 
    return replicaTablero 
 
  
def obtenerJugadasValidas(tablero, baldosa): 
    # Devuelve una lista de listas [x,y] de jugadas válidas para el jugador en el tablero dado. 
    jugadasValidas = [] 
 
    for x in range(8): 
        for y in range(8): 
            if esJugadaValida(tablero, baldosa, x, y) != False: 
                jugadasValidas.append([x, y]) 
    return jugadasValidas 
  
  
def obtenerPuntajeTablero(tablero): 
    # Determina el puntaje contando las piezas. Devuelve un diccionario con claves 'X' y 'O'.