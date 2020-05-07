from Agente import Agente
import random


print('Agentes\n')
# Variables del script
n = 14              #   Agentes
m = 7               #   Objetos
max_t = 1000        #   Iteraciones máximas
P=[]                #   Población de agentes
it=0                #   Contador de iteraciones



# Función que retorna las métricas solicitadas para el algoritmo
def metricas_iteracion():
    # Variables para métricas de nombres conocidos
    lista_Conocidos=[]
    n_Nombres_Conocidos = 0
    # Variables para métricas del número total de nombres por objeto
    l_Nombres_Objeto = ""
    n_Nombres_Objeto = ""
    # Variables para métricas del promedio de longitud de todos los nombres
    n_Suma_Long = 0
    n_Tot_Nombres = 0
    
    # Recorrer todos los agentes para obtener sus objetos
    for i in P:
        objetos = i.obj
        n_Nombres_Objeto+="\n\tAgente "+str(P.index(i)+1)+"\t->"
        for j in objetos:
            n_Nombres_Objeto+="\tObjeto "+str(objetos.index(j)+1)+" = "+str(len(j))
            n_Tot_Nombres = n_Tot_Nombres + len(j)
            for k in j:
                n_Suma_Long = n_Suma_Long + len(k)
                # Buscar conocidos
                if k not in lista_Conocidos:
                    lista_Conocidos.append(k)
                    n_Nombres_Conocidos = n_Nombres_Conocidos + 1    

    l_Nombres_Objeto+=n_Nombres_Objeto
    promedio = str(round((n_Suma_Long/n_Tot_Nombres),2))

    return {
        "n_Conocidos":n_Nombres_Conocidos,
        "n_Nom_Objetos":l_Nombres_Objeto,
        "n_Prom_Long":promedio
    }
    

# Crear población de agentes
for i in range(n):
    P.append(Agente(m))



# Iniciar las iteraciones
for i in range(max_t):
    # Contador de iteraciones
    it=it+1
    
    # Obtener identificador de agentes aleatorios no repetibles
    n_h = random.randint(0,n-1)
    n_o = random.randint(0,n-1)
    while (n_h == n_o):
        n_o=random.randint(0,n-1)

    # Objeto aleatorio
    k=random.randint(0,m-1)

    # Creación de hablante y oyente
    hablante = P[n_h]
    oyente = P[n_o]

    # Hablante enuncia
    hablante.enunciar(k,oyente)

    # Imprimir solo iteraciones 1-10 y 995 a 1000
    if(it<=10 or it>995):
        # Obtención de las métricas
        m_it = metricas_iteracion()
        # Presentación en pantalla de las métricas
        print('\n\n------------------------------------------------------------------------')
        print('Iteración #:\t'+str(it))
        print('Nombres conocidos: '+str(m_it['n_Conocidos']))
        print('Nombres por cada objeto: '+m_it['n_Nom_Objetos'])
        print('Longitud promedio de los nombres: '+m_it['n_Prom_Long'])
