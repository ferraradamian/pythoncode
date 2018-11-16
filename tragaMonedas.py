#juego traga monedas

import random
import time

creditos = 5
tablero = [['X','O','$'],['X','O','$'],['X','O','$']]

def tableroAzar(tablero):  
    for i in range(3):
        lista = ['X','O','$']
        random.shuffle(lista)
        tablero[i] = lista

def imprimirTablero(tablero):
    print('      ------------------')    
    for i in range(3):       
        for j in range(3):
            print('       ',end='')
            print(tablero[j][i],end='')
        print()
    print('      ------------------')    
    print()    

def pedirJugada():
    print('tira la ruleta')
    input()
    time.sleep(0.2)
    print()
    
def aciertaFila(tablero, creditos):
    CreditosGanados = 0   
    for i in range(3): 
        fila = ''      
        for j in range(3):
            fila += tablero[j][i]

        if fila == '$$$':
            CreditosGanados += 5
            print('Acertaste una fila con $$$ sumas: ¡5 creditos!')
        elif fila == 'XXX':
            CreditosGanados += 2
            print('Acertaste una fila con XXX sumas: ¡2 creditos!')
        elif fila == 'OOO':
            CreditosGanados += 1
            print('Acertaste una fila con OOO sumas: ¡1 creditos!')
                               
    print()
    return CreditosGanados + creditos

def imprimirCreditos(creditos):
    print('     ',end='')
    print('--------------------')
    print('     ',end='')
    print('Tus creditos son: %s' %(creditos))
    print('     ',end='')
    print('--------------------')

def jugarDeNuevo(): 
    # Esta función devuelve True si el jugador quiere volver a jugar, en caso contrario devuelve False. 
    print('¿Quieres jugar de nuevo? (sí o no)') 
    return input().lower().startswith('s')    

while True: 
    imprimirCreditos(creditos) 
    tableroAzar(tablero)    
    pedirJugada()
    imprimirTablero(tablero)
    creditos = aciertaFila(tablero, creditos)
    creditos -= 1
    if creditos == 0:
        print('¡Te has quedado sin credito!')  
        print()
        if jugarDeNuevo(): 
            creditos = 6     
        else: 
            break    
        

