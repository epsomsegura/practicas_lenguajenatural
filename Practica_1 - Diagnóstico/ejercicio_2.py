# Universidad Veracruzana
# Maestría en Sistemas Interactivos Centrados en el Usuario
# Experiencia educativa: Lenguaje Natural
# Practica: 1
# Ejercicio: 2
# Descripción: Lenguaje de la F
# Por: Epsom Enrique Segura Jaramillo


def vocals():
    vocals=dict()
    vocals['a']='afa'
    vocals['e']='efe'
    vocals['i']='ifi'
    vocals['o']='ofo'
    vocals['u']='ufu'
    vocals['á']='áfa'
    vocals['é']='éfe'
    vocals['í']='ífi'
    vocals['ó']='ófo'
    vocals['ú']='úfu'
    vocals['ü']='üfu'
    vocals['y']='yfi'

    return vocals

def translateWords(phrase):
    newPhrase = ""
    arr_words = phrase.split()
    # Separar palabras por espacio
    for w in arr_words:
        if w == 'y':
            newPhrase+=vocals()[w]+" "
        else:
            newWord=""
            for l in w:
                if l in vocals().keys():
                    newWord+=vocals()[l]
                else:
                    newWord+=l
            newPhrase+=newWord+" "
    
    return newPhrase
    



print("Lenguaje de la F\n")
phrase = input('Ingresa una frase y la cambiaré al lenguaje de la "F": ').lower()
newPhrase = translateWords(phrase)
print("\n"+newPhrase)





