# Universidad Veracruzana
# Maestría en Sistemas Interactivos Centrados en el Usuario
# Experiencia educativa: Lenguaje Natural
# Practica: 1
# Ejercicio: 1
# Descripción: Suma de enteros
# Por: Epsom Enrique Segura Jaramillo


print("Sumar una secuencia de números\n")
sum=0
n = input('Ingresa un número: ')
for x in range(int(n)):
    sum+=x+1

print('\nLa suma de los números del 1 al '+n+' es: '+str(sum))
