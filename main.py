# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import math
import random


def mcd(n1, n2):
    if (n1 > n2):
        for i in range(1, n1):
            if n1 % i == 0 and n2 % i == 0:
                cont1 = i
        return cont1
    else:
        for i in range(1, n2):
            if n1 % i == 0 and n2 % i == 0:
                cont2 = i
        return cont2

print(mcd(20, 30))

def exponente (n):
    for i in range (0,n+1):
        cont = 2**i
        if (cont > n):
            return i-1

print (exponente(64))

def panprimo (n):
    contador = 0
    for i in range (1,(n % 1000)+1):
        if ((n % 1000) % i == 0):
            contador +=1
    if contador > 2:
        return False
    cadena = str(n)
    for i in range (0,10):
        a = str(i)
        if a not in cadena:
            return False
    return True

print(panprimo(1234567809687833242341))