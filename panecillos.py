import random
def obtenerNumSecreto(digitosNum):
    # Devuelve un numero de largo digotosNUm, compuesto de dígitos únicos al azar.
    numeros = list(range(10))
    random.shuffle(numeros)
    numSecreto = ''
    for i in range(digitosNum):
        numSecreto += str(numeros[i])
    