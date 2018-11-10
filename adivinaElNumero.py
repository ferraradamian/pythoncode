#Este es el juego de adivinar el numero
import random

intentosRealizados = 0

print('¡Hola!, ¿como te llamas?')
miNombre = input()

nuemero = random.randint(1,20)
print('Bueno, '+miNombre+', estoy pensando un numero entre 1 y 20')

while intentosRealizados < 6:
    print('intenta adivinar') #hay cuatro espacios delante del print.
    estimacion = input()
    estimacion = int(estimacion)

    intentosRealizados = intentosRealizados + 1

    if estimacion < nuemero:
        print('Tu estimacion es muy baja')
    if estimacion > nuemero:
        print('Tu estimacion es muy alta')
    if estimacion == nuemero:
        break

if estimacion == nuemero:
    intentosRealizados = str(intentosRealizados)
    print('¡Buen trabajo, '+miNombre+'!¡Has adivinado mi numero en '+intentosRealizados+' intentos!')

if estimacion != nuemero:
    nuemero = str(nuemero)
    print('Pues no. el numero que estaba pensando era '+ nuemero)    
