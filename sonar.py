# Sonar 
  
import random 
import sys 
  
def dibujarTablero(tablero): 
    # Dibuja la estructura de datos del tablero. 
  
    líneah = '    ' # espacio inicial para los números a lo largo del lado izquierdo del tablero 
    for i in range(1, 6): 
        líneah += (' ' * 9) + str(i) 

    # imprimir los números a lo largo del borde superior 
    print(líneah) 
    print('   ' + ('0123456789' * 6)) 
    print() 
 
    # imprimir cada una de las 15 filas 
    for i in range(15): 
        # los números de una sola cifra deben ser precedidos por un espacio extra 
        if i < 10: 
            espacioExtra = ' ' 
        else: 
            espacioExtra = '' 
        print('%s%s %s %s' % (espacioExtra, i, obtenerFila(tablero, i), i)) 
   
    # imprimir los números a lo largo del borde inferior 
    print() 
    print('   ' + ('0123456789' * 6)) 
    print(líneah)   


def obtenerFila(tablero, fila):
    # Devuelve una cadena con la estructura de datos de un tablero para una fila determinada.
    filaTablero = ''
    for i in range(60):
        filaTablero += tablero[i][fila]
    return filaTablero

def obtenerNuevoTablero():
    # Devuelve una cadena con la estructura de datos de un tablero para una fila determinada.
    tablero = []
    for x in range(60):# la lista principal es una lista de 60 listas 
        tablero.append([])
        for y in range(15):# cada lista en la lista principal tiene 15 cadenas de un solo caracter 
            # usar diferentes caracteres para el océano para hacerlo más fácil de leer.
            if random.randint(0,1) == 0:
                tablero[x].append('~')
            else:
                tablero[x].append('`')               
    return tablero            