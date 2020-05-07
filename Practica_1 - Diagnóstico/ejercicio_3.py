# Universidad Veracruzana
# Maestría en Sistemas Interactivos Centrados en el Usuario
# Experiencia educativa: Lenguaje Natural
# Practica: 1
# Ejercicio: 3
# Descripción: Juego de ahorcado
# Por: Epsom Enrique Segura Jaramillo

import re


class Ahorcado:
    word=""
    max_error=0
    e=1
    c_list_ok=list()
    c_list_no=list()

    def __init__(self,word,max_error):
        self.word = word
        self.max_error = max_error
        self.e = 0
        self.c_list_ok=list()

        self.instrucciones()

        self.estado()
        
    
    def jugar(self,c):
        if(len(c)>1):
            print('Solo debes ingresar un caracter\n')
        else:
            if (re.match(r"^[A-Za-z]*$",c)):
                if(c in self.c_list_ok):
                    print('Ya intentaste con esa letra\n')
                    self.e+=1
                else:
                    if (c not in self.word):
                        self.c_list_ok.append(c)
                        self.e+=1
                    self.c_list_ok.append(c)
            else:
                print('Solo debes ingresar letras\n')
                
        self.estado()



    def estado(self):
        tmp=0
        x=""
        for i in self.word:
            if(len(self.c_list_ok)<1):
                x+='_ '
            else:
                if i in self.c_list_ok:
                    x+=i+' '
                    tmp+=1
                else:
                    x+='_ '
                    
        x+=' ('+str((self.max_error-self.e))+' errores posibles)\n'
        print(x)

        if(self.e >= self.max_error):
            y=""
            for c in self.word:
                y+=c+' '
            y+=' (Perdiste)'
            print(y)
        elif(len(self.word)==tmp):
            print("Ganaste")
        else:
            c = input('Introduce una letra: ')
            self.jugar(c)

    
    def instrucciones(self):
        print('Juego de ahorcado\n\nInstrucciones: \n\t-Adivina la palabra con el menor número de errores.\n\t-Solo debes ingresar una letra\n\nComencemos:\n\n')
