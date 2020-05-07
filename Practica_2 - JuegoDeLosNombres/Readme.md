
# Lenguaje Natural
## Práctica 2 - Juego de las palabras

### Introducción
La presente práctica se basa en conocer como agentes pueden crear y mantener nombres para una cantidad de objetos asignados a cada uno.
La implementación del algoritmo se basa en elegir dos agentes al azár. Uno toma el rol de hablante, el cual se encarga de dar una palabra al otro agente, misma que busca en una lista de un objeto especifico el cual es asignado al momento de elegir ambos agentes, si su lista está vacía, el agente hablante debe crear un nuevo nombre el cual está constituido por máximo ocho sílabas, cada sílaba inicia con una consonante y termina con una vocal. El segundo agente o agente oyente escucha el nombre que le enuncia el agente hablante, si el agente oyente conoce el nombre genera una respuesta positiva, de lo contrario retorna una respuesta negativa y almacena el nombre en su inventario de nombres.

### Descripción de la carpeta
La práctica fue cargada en el repositorio principal de las actividades del ciclo escolar, el nombre del directorio del repositorio asignado a esta practica es `Practica_2 - JuegoDeLasPalabras`, el cual almacena los siguientes ficheros:

- Agente.py
- Script.py
- Readme.py

### Descripción de los ficheros
El fichero `Agente.py` contiene la clase Agente, el cual contiene la propiedad de tener un número `m` de objetos, y contiene los métodos: 
- **silaba**: Encargado de retornar una sílaba de dos letras, la cual inicia con una consonante y termina con una vocal, ambas letras seleccionadas de manera aleatoria.
- **nombrar**: Encargado de retornar un nombre de máximo ocho silabas, la cantidad de silabas se genera de manera aleatoria.
- **enunciar**: Encargado de retornar un valor booleano obtenido del resultado de evaluar la existencia de un nombre en el inventario de objetos de un `segundo agente` recibido como parámetro de este método, el `objeto` es seleccionado mediante un parámetro recibido en este método. Este método también evalua la existencia de un nombre en el `primer agente`, si el inventario del objeto está vacío, genera un nombre aleatorio y lo almacena para realizar la actividad antes mencionada.

El fichero `Script.py`se encarga de ejecutar la prueba de funcionamiento del algoritmo que contiene la clase `Agente`. Dentro de este script se indica que se desea crear una población `P` de 14 agentes, cada agente tiene 7 objetos `m` y se desea iterar como máximo `max_t` 1000 veces. Cada iteración debe mostrar en pantalla la `cantidad de nombres conocidos`, la `cantidad de nombres por cada objeto`, la `longitud promedio de todos los nombres` y el `número de iteración`.



### Ejecución del algoritmo
A continuación se presenta un ejemplo de los resultados de ejecutar el algoritmo en 1000 iteraciones, cabe mencionar que se habilitó el siguiente fragmento de código quitando los comentarios:
````
Fragmento de código encontrado en el fichero Script.py

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
````

### Resultado
A continuación se muestra el resultado de la ejecución del algoritmo de la práctica:
````
Agentes



------------------------------------------------------------------------
Iteración #:	1
Nombres conocidos: 1
Nombres por cada objeto: 
	Agente 1	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 2	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 4 = 1	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 3	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 4	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 5	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 6	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 7	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 8	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 9	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 10	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 11	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 12	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 13	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 4 = 1	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 14	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
Longitud promedio de los nombres: 8.0


------------------------------------------------------------------------
Iteración #:	2
Nombres conocidos: 2
Nombres por cada objeto: 
	Agente 1	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 2	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 4 = 1	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 3	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 4	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 5	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 6	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 7	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 8	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 9	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 10	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 4 = 1	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 11	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 12	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 4 = 1	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 13	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 4 = 1	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 14	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
Longitud promedio de los nombres: 10.0


------------------------------------------------------------------------
Iteración #:	3
Nombres conocidos: 3
Nombres por cada objeto: 
	Agente 1	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 2	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 4 = 1	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 3	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 4	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 5	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 6	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 7	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 8	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 9	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 10	->	Objeto 1 = 1	Objeto 2 = 0	Objeto 2 = 0	Objeto 4 = 1	Objeto 2 = 0	Objeto 2 = 0	Objeto 2 = 0
	Agente 11	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 12	->	Objeto 1 = 1	Objeto 2 = 0	Objeto 2 = 0	Objeto 4 = 1	Objeto 2 = 0	Objeto 2 = 0	Objeto 2 = 0
	Agente 13	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 4 = 1	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 14	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
Longitud promedio de los nombres: 11.33


------------------------------------------------------------------------
Iteración #:	4
Nombres conocidos: 4
Nombres por cada objeto: 
	Agente 1	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 2	->	Objeto 1 = 0	Objeto 2 = 1	Objeto 1 = 0	Objeto 4 = 1	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 3	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 4	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 5	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 6	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 7	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 8	->	Objeto 1 = 0	Objeto 2 = 1	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 9	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 10	->	Objeto 1 = 1	Objeto 2 = 0	Objeto 2 = 0	Objeto 4 = 1	Objeto 2 = 0	Objeto 2 = 0	Objeto 2 = 0
	Agente 11	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 12	->	Objeto 1 = 1	Objeto 2 = 0	Objeto 2 = 0	Objeto 4 = 1	Objeto 2 = 0	Objeto 2 = 0	Objeto 2 = 0
	Agente 13	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 4 = 1	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 14	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
Longitud promedio de los nombres: 10.0


------------------------------------------------------------------------
Iteración #:	5
Nombres conocidos: 5
Nombres por cada objeto: 
	Agente 1	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 2	->	Objeto 1 = 0	Objeto 2 = 1	Objeto 1 = 0	Objeto 4 = 1	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 3	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 4 = 1	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 4	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 5	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 6	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 7	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 8	->	Objeto 1 = 0	Objeto 2 = 1	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 9	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 10	->	Objeto 1 = 1	Objeto 2 = 0	Objeto 2 = 0	Objeto 4 = 2	Objeto 2 = 0	Objeto 2 = 0	Objeto 2 = 0
	Agente 11	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 12	->	Objeto 1 = 1	Objeto 2 = 0	Objeto 2 = 0	Objeto 4 = 1	Objeto 2 = 0	Objeto 2 = 0	Objeto 2 = 0
	Agente 13	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 4 = 1	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 14	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
Longitud promedio de los nombres: 8.4


------------------------------------------------------------------------
Iteración #:	6
Nombres conocidos: 6
Nombres por cada objeto: 
	Agente 1	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 2	->	Objeto 1 = 0	Objeto 2 = 1	Objeto 1 = 0	Objeto 4 = 1	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 3	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 4 = 1	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 4	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 5	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 6	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 7	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 8	->	Objeto 1 = 0	Objeto 2 = 1	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 9	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 3 = 1	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 10	->	Objeto 1 = 1	Objeto 2 = 0	Objeto 2 = 0	Objeto 4 = 2	Objeto 2 = 0	Objeto 2 = 0	Objeto 2 = 0
	Agente 11	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 12	->	Objeto 1 = 1	Objeto 2 = 0	Objeto 2 = 0	Objeto 4 = 1	Objeto 2 = 0	Objeto 2 = 0	Objeto 2 = 0
	Agente 13	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 3 = 1	Objeto 4 = 1	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 14	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
Longitud promedio de los nombres: 7.33


------------------------------------------------------------------------
Iteración #:	7
Nombres conocidos: 7
Nombres por cada objeto: 
	Agente 1	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 4 = 1	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 2	->	Objeto 1 = 0	Objeto 2 = 1	Objeto 1 = 0	Objeto 4 = 1	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 3	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 4 = 1	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 4	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 5	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 4 = 1	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 6	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 7	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 8	->	Objeto 1 = 0	Objeto 2 = 1	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 9	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 3 = 1	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 10	->	Objeto 1 = 1	Objeto 2 = 0	Objeto 2 = 0	Objeto 4 = 2	Objeto 2 = 0	Objeto 2 = 0	Objeto 2 = 0
	Agente 11	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 12	->	Objeto 1 = 1	Objeto 2 = 0	Objeto 2 = 0	Objeto 4 = 1	Objeto 2 = 0	Objeto 2 = 0	Objeto 2 = 0
	Agente 13	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 3 = 1	Objeto 4 = 1	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 14	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
Longitud promedio de los nombres: 7.43


------------------------------------------------------------------------
Iteración #:	8
Nombres conocidos: 7
Nombres por cada objeto: 
	Agente 1	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 4 = 1	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 2	->	Objeto 1 = 0	Objeto 2 = 1	Objeto 1 = 0	Objeto 4 = 1	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 3	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 4 = 1	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 4	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 4 = 1	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 5	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 4 = 1	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 6	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 7	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 8	->	Objeto 1 = 0	Objeto 2 = 1	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 9	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 3 = 1	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 10	->	Objeto 1 = 1	Objeto 2 = 0	Objeto 2 = 0	Objeto 4 = 2	Objeto 2 = 0	Objeto 2 = 0	Objeto 2 = 0
	Agente 11	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 12	->	Objeto 1 = 1	Objeto 2 = 0	Objeto 2 = 0	Objeto 4 = 1	Objeto 2 = 0	Objeto 2 = 0	Objeto 2 = 0
	Agente 13	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 3 = 1	Objeto 4 = 1	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 14	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
Longitud promedio de los nombres: 7.47


------------------------------------------------------------------------
Iteración #:	9
Nombres conocidos: 8
Nombres por cada objeto: 
	Agente 1	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 4 = 1	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 2	->	Objeto 1 = 0	Objeto 2 = 1	Objeto 1 = 0	Objeto 4 = 1	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 3	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 4 = 1	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 4	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 4 = 1	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 5	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 4 = 1	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 6	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 4 = 1	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 7	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 4 = 1	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 8	->	Objeto 1 = 0	Objeto 2 = 1	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 9	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 3 = 1	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 10	->	Objeto 1 = 1	Objeto 2 = 0	Objeto 2 = 0	Objeto 4 = 2	Objeto 2 = 0	Objeto 2 = 0	Objeto 2 = 0
	Agente 11	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 12	->	Objeto 1 = 1	Objeto 2 = 0	Objeto 2 = 0	Objeto 4 = 1	Objeto 2 = 0	Objeto 2 = 0	Objeto 2 = 0
	Agente 13	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 3 = 1	Objeto 4 = 1	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 14	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
Longitud promedio de los nombres: 8.24


------------------------------------------------------------------------
Iteración #:	10
Nombres conocidos: 9
Nombres por cada objeto: 
	Agente 1	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 4 = 1	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 2	->	Objeto 1 = 0	Objeto 2 = 1	Objeto 1 = 0	Objeto 4 = 1	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 3	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 4 = 1	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 4	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 4 = 1	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 5	->	Objeto 1 = 0	Objeto 2 = 1	Objeto 1 = 0	Objeto 4 = 1	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 6	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 4 = 1	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 7	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 4 = 1	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 8	->	Objeto 1 = 0	Objeto 2 = 1	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 9	->	Objeto 1 = 0	Objeto 2 = 1	Objeto 3 = 1	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 10	->	Objeto 1 = 1	Objeto 2 = 0	Objeto 2 = 0	Objeto 4 = 2	Objeto 2 = 0	Objeto 2 = 0	Objeto 2 = 0
	Agente 11	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 12	->	Objeto 1 = 1	Objeto 2 = 0	Objeto 2 = 0	Objeto 4 = 1	Objeto 2 = 0	Objeto 2 = 0	Objeto 2 = 0
	Agente 13	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 3 = 1	Objeto 4 = 1	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
	Agente 14	->	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0	Objeto 1 = 0
Longitud promedio de los nombres: 8.63


------------------------------------------------------------------------
Iteración #:	996
Nombres conocidos: 7
Nombres por cada objeto: 
	Agente 1	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 2	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 3	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 4	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 5	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 6	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 7	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 8	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 9	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 10	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 11	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 12	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 13	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 14	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
Longitud promedio de los nombres: 5.71


------------------------------------------------------------------------
Iteración #:	997
Nombres conocidos: 7
Nombres por cada objeto: 
	Agente 1	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 2	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 3	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 4	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 5	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 6	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 7	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 8	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 9	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 10	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 11	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 12	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 13	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 14	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
Longitud promedio de los nombres: 5.71


------------------------------------------------------------------------
Iteración #:	998
Nombres conocidos: 7
Nombres por cada objeto: 
	Agente 1	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 2	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 3	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 4	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 5	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 6	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 7	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 8	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 9	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 10	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 11	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 12	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 13	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 14	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
Longitud promedio de los nombres: 5.71


------------------------------------------------------------------------
Iteración #:	999
Nombres conocidos: 7
Nombres por cada objeto: 
	Agente 1	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 2	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 3	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 4	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 5	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 6	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 7	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 8	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 9	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 10	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 11	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 12	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 13	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 14	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
Longitud promedio de los nombres: 5.71


------------------------------------------------------------------------
Iteración #:	1000
Nombres conocidos: 7
Nombres por cada objeto: 
	Agente 1	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 2	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 3	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 4	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 5	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 6	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 7	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 8	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 9	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 10	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 11	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 12	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 13	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
	Agente 14	->	Objeto 1 = 1	Objeto 2 = 1	Objeto 3 = 1	Objeto 4 = 1	Objeto 5 = 1	Objeto 6 = 1	Objeto 7 = 1
Longitud promedio de los nombres: 5.71
````
###### Autor
Epsom Erique Segura Jaramillo