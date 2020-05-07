import math

print('Distancia de Hamming\n')

n = input('Ingresa el texto 1: ')
m = input('Ingresa el texto 2: ')

dH=0

if len(n)==len(m):
    for i in range(len(n)):
        dH = (dH+0) if (n[i]==m[i]) else dH+1
    
    print('La distancia de Hamming es: '+str(dH))
else:
    print('Las cadenas deben ser del mismo tamaño')






