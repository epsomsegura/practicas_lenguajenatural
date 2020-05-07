# Universidad Veracruzana
# Maestría en Sistemas Interactivos Centrados en el Usuario
# Experiencia educativa: Lenguaje Natural
# Practica: 2
# Ejercicio: 1
# Descripción: Juego de nombres
# Por: Epsom Enrique Segura Jaramillo

import random

class Agente:
    vocales = "aeiou"
    consonantes = "bcdfghjklmnpqrstvwxyz"

    # Constructor
    def __init__(self,m):
        # Número de objetos
        self.m=m
        self.obj=[[] for i in range(m)]

    # Método nombrar
    def nombrar(self):
        nombre = ""
        rand=random.randint(1,8)
        for i in range(rand):
            nombre=nombre+self.silaba()

        return nombre

    # Método enunciar
    def enunciar(self,k,a):
        resp = False
        nombre = self.nombrar()
        
        # Inventar nombre si no existe
        if len(self.obj[k])==0:
            # print('******** EL NOMBRE ES INVENTADO ********')
            self.obj[k].append(nombre)
        else:
            ln_menor=16
            for i in self.obj[k]:
                if len(i) < ln_menor:
                    nombre = i
            # print('******** EL NOMBRE ES ENCONTRADO ********')

        # Validar el conocimiento del nombre
        if nombre in a.obj[k]:
            # print('******** EL NOMBRE COINCIDE ********')
            self.obj[k]=[nombre]
            a.obj[k]=[nombre]

            resp = True
        else:
            # print('******** EL NOMBRE SE AGREGA ********')
            a.obj[k].append(nombre)
            resp = False

        return resp


    # Método para generar silabas
    def silaba(self):
        consonante = random.choice(self.consonantes)
        vocal = random.choice(self.vocales)
        return consonante+vocal