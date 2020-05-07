# Universidad Veracruzana
# Maestría en Sistemas Interactivos Centrados en el Usuario
# Experiencia educativa: Lenguaje Natural
# Practica: 1
# Ejercicio: 3.1
# Descripción: Juego de ahorcado
# Por: Epsom Enrique Segura Jaramillo

# Paquetes
import random
import os
from ejercicio_3 import Ahorcado as a

# Lista de palabras
arr_words=list()
base=(os.path.realpath(__file__)).rsplit('/',1)[0]
w_file = open(base+'/src/listado-general.txt','r')
for w in w_file:
    arr_words.append(w[:-1])
w_file.close()

# Configuraciones del juego
word = random.choice(arr_words)
error = int(random.uniform(3,7))

a(word,error)