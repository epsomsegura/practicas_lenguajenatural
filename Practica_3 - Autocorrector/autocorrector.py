import os
import nltk
import re
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from nltk.metrics.distance import edit_distance
from text_analysis import text_analysis
from datetime import datetime

# Leer el listado general
def listadoGeneral(f_lista):
    fp = open(f_lista,'r',encoding="utf-8-sig")
    lineas = fp.readlines()
    fp.close()

    for i in lineas:
        datos.add(i.rstrip('\n').lower())

def lematizacion(f_lemas):
    fp = open(f_lemas,'r',encoding="utf-8-sig")
    lineas = fp.readlines()
    fp.close()
    for i in lineas:
        temp = i.rstrip("\n")
        lp = temp.replace("\t","-").split('-')
        datos.add(lp[0].lower())
        datos.add(lp[1].lower())

# Variables
f_texto = "./src/corrigeme.txt"
f_lemas = "./src/lemmatization-es.txt"
f_lista = "./src/listado-general.txt"

# Instancia a clase
t=text_analysis(f_texto)

# Crear tokens
datos = set()
texto = t.readText(f_texto)
# Expresión regular para buscar alfanuméricos
# regexp = r"^[üá-úÁ-Úa-zA-Z0-9].*$"
r_exp_an = "^[Á-Úüá-úa-zA-Z0-9]*$"
r_exp_n = "^[0-9\.\0-9]*$"

# Obtener palabras funcionales
stopwords = t.getStopwords()

# Creación de diccionario
listadoGeneral(f_lista)
lematizacion(f_lemas)


toktok = ToktokTokenizer()
es_tokenizador_oraciones = nltk.data.load('tokenizers/punkt/spanish.pickle')
oraciones = es_tokenizador_oraciones.tokenize(texto)

texto=""
corregido = open("src/corregido.txt","w")
for s in oraciones:
    r_oraciones=[]
    for i in toktok.tokenize(s):
        if re.match(r_exp_an,i):
            print("Prueba REGEXP start:\t",end = "")
            if i.lower() in stopwords:
                r_oraciones.append(i)
                print('Prueba Stopwords OK:',i)
            elif re.match(r_exp_n,i):
                r_oraciones.append(i)
                print('Prueba REGEXP-Numbers OK:',i)
            else:
                print("Buscar "+str(i)+": ")
                x = None
                rnk = 3
                for j in datos:
                    if(len(i)+3)>=len(j):
                        distancia = edit_distance(i.lower(),j)
                        if(distancia < rnk):
                            rnk=distancia
                            if(rnk == 0):
                                x=j
                                print(i,j,distancia,rnk,x,str((len(i)+3)),str(len(j)),(len(i)+3)>=len(j))
                                break
                            else:
                                x=j if (rnk<2) else None
                if x==None:
                    print('\tCambiado->No')
                    r_oraciones.append(i)
                else:
                    print('\tCambiado->Si: '+x)
                    r_oraciones.append(x)
        elif not re.match(r_exp_an,i):
            print('Prueba REGEXP No:',i)
            r_oraciones.append(i)


    print('oración revisada')
    separador = " "
    oracion = separador.join(r_oraciones)
    texto=texto+oracion+"\n"

corregido.write(texto)
corregido.close()