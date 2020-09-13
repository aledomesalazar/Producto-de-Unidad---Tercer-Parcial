# Producto de Unidad - Tercer Parcial
## Aplicación de la máquina de estados en probelmas reales

**1. PLANTEAMIENTO DEL PROBLEMA**

*1.1 Contexto y antecedentes*

La máquina de estado se define como un circuito secuencial con un comportamiento reflejado en distintos estados, dependiendo de las entradas y estado actual. Se utiliza para crear aplicaciones donde existen estados distinguibles, donde cada estado puede llevar a uno o varios estados y puede finalizar el flujo del proceso.
Es importante señalar que muchas aplicaciones requieren un estado de "inicialización" seguido de un estado predeterminado, donde se puede realizar muchas acciones diferentes. Estas acciones dependen de las entradas anteriores y actuales, así como de los estados.
Al diseñar máquinas de estados se puede crear un diagrama de estado para representar gráficamente los diferentes estados y cómo interactúan para modelar los algoritmos de control que necesita con estados lógicos discretos.
Los circuitos secuenciales tienen un número determinado de estados (2^n). Pueden ser:
– Retroalimentados (flip-flops, biestables) 
– Máquinas sincrónicas temporizadas
Así también las máquinas de estados se clasifican en dos:
a)	Máquinas de Moore: es un circuito secuencial donde las salidas dependen del estado presente mas no de las entradas. 
b)	Máquinas de Mealy: es un circuito secuencial con un comportamiento reflejado en diferentes estados dependiendo de las entradas y su estado actual, siempre gobernado por una señal de reloj. Podrá disponer de salidas que especifican su propósito.

*1.2 Formulación del problema*

Conocer el funcionamiento y clasificación de las máquinas de estado para su aplicación en la resolución de problemas secuenciales. 

*1.3 Hipótesis de Investigación*

Aplicación de diagramas de máquinas de estado permite una correcta interpretación de la lógica del circuito y su funcionamiento.

**2. OBJETIVOS**

**2.1. Objetivo General**

Construir y resolver máquinas de estados, a través de diagramas y tablas de verdad para una mejor interpretación del funcionamiento de la máquina.

**2.2. Objetivos Específicos**
-	Interpretar las tablas de estados realizando un diagrama con el fin de crear una máquina de estados finito.
-	Convertir el diagrama de estados en una tabla a fin de tener una mayor interpretación en la operatividad de una máquina de estado. 

**3. ESTADO DEL ARTE**

*Design of the Software Architecture for Starcraft Video Game on the Basis of Finite State Machine*

Los investigadores Ivan Y. Smolyakov y Sergey A. Belyaev de la Universidad Electrónica Saint-Petersburg realizaron en el año 2019 un artículo exponiendo cual sería el mejor método de resolución del videojuego Starcraft. Los autores del videojuego proponen diferentes enfoques para poder resolver el juego; uno de ellos es la coordinación de agentes radiales independientes, pero también seleccionan el enfoque clásico de las maquinas finitas de estados. Este enfoque viene combinado con la utilización de árboles de decisión. Los resultados mostraron las ventajas y las limitaciones de cada enfoque discutido en el artículo. (Smolyakov & Belyaev, 2019) 

*Structural Representation of Synthesis Methods of Finite State Machine with Datapath of Transitions*

Roman Babakov y Alexander Barkalov, investigadores de la Universidad de Zielona en Polonia, realizaron en el año 2018 un artículo donde exponen diferentes métodos para representar una máquina de estados finita con una ruta de datos de transiciones. Para una mejor síntesis de la quina de estados finita se debe definir bien las condiciones que se vayan a tomar, esto debido a que las condiciones determinan el diseño. Las componentes de la estructura son elementos del modelo a utilizar para la máquina de estados finita con ruta de datos de transiciones.  (Babakov & Barkalov, 2018)

*A Test Generation Method Based on k-Cycle Testing for Finite State Machines*

Yuya Kinoshita, Toshinori Hosokawa y Hideo Fujiwara, investigadores de la Universidad Osaka Gakuin en Japón, realizaron en el año de 2019 un artículo que propone un método para evitar las desventajas en las pruebas de escaneo. Estas pruebas requieren un tiempo de aplicación de prueba prolongado y una gran sobrecarga de hardware. El método propuesto es un modelo de expansión de tiempo con restricciones de estado inicial para controladores y un método de generación de pruebas basado en máquinas de estados finitos. (Kinoshita, Hosokawa, & Fujiwara, 2019)

**4. MARCO TEÓRICO**

**4.1. Máquinas de estados finitos**

Una máquina de estados finito es una representación abstracta para manipular símbolos con la finalidad de conocer si una cadena pertenece a un lenguaje o se puede utilizar de forma indistinta. Las máquinas de estados se caracterizan por tener un estado inicial, son capaces de recibir una cadena de símbolos, pueden cambiar de estado por cada elemento leído o pueden permanecer en el mismo estado. Además, tienen un conjunto de estados finales que indican si una cadena pertenece al lenguaje al final de una lectura.
Existen dos tipos de máquinas de estado, las maquinas finitas deterministas y maquinas finitas no deterministas.

*4.1.1. Máquinas Finitas Determinísticas*

Estas máquinas reciben de forma secuencial una cadena de símbolos y cambia de estado por cada símbolo leído o también puede permanecer en el mismo estado. Al final de la lectura del estado, la máquina de estados indica si la cadena es aceptada o pertenece al lenguaje que describe la máquina. Si al final de leer todos los símbolos de entrada la maquina está en alguno de los estados finales entonces esa cadena es aceptada, si el estado no es final entonces la cadena no pertenece al lenguaje.

Los componentes que definen una maquina finita determinista son: 

A={Q,q0,F,δ,∑}

Donde: 

Q: conjunto finito de estados

q0: estado inicial

F: conjunto finito de estados finales 

∑: alfabeto finito de entrada

δ: función de transición

La forma más sencilla de comprender una maquina finita es a través de un diagrama de transición. Un diagrama de transición es un dígrafo etiquetado con los elementos de una máquina de estados finito. Con esta representación de puede representar cualquier máquina de estados finito determinista, como se muestra a continuación.

![]()

**Figura 1. Diagrama de transición o dígrafo**

En un diagrama de transición existe un nodo por cada estado de Q. Los estados finales están encerrados en un círculo doble. El estado inicial es apuntado por una flecha que no proviene de ningún otro estado. Para cada estado hay exactamente una y sólo una flecha que inicia en un estado y termina en otro estado.

Para describir por completo una función de transición se ocupa una Tabla de Transición. Las columnas se etiquetan con los símbolos de entrada; las filas son etiquetadas con los estados y en las intersecciones se colocan los nuevos estados, como se muestra en la figura a continuación. 

![]()

**Figura 2. Tabla de transición**

Para determinar que una máquina de estados sea una maquina determinista cada estado debe tener el mismo número de flechas saliendo de cada uno de ellos. 

*4.1.2. Máquinas Finitas No Determinísticas*

A diferencia de las maquinas finitas deterministas, donde existe una única forma de llegar de un estado a otro con una entrada y se tiene solo un estado inicial, las maquinas finitas no deterministas no cuentan con estas virtudes, pero son una herramienta de mucha ayuda cuando se requiere diseñar una maquina determinista. Para cada máquina no determinista existe una maquina determinista que lo representa y que acepta el mismo lenguaje. 

Los componentes que definen una maquina finita no determinista son: 

A = {Q,I,F,δ,∑}

Donde: 

Q: conjunto finito de estados

I: conjunto de estados iniciales 

F: conjunto finito de estados finales 

∑: alfabeto finito de entrada

δ: función de transición

Aparentemente existe similitud con una maquina determinista, pero existen diferencias. En las maquinas no deterministas puede existir más de un estado inicial y la función de transición entrega un conjunto de posibles estados. Precisamente esta es la diferencia entre una maquina determinista y una maquina no determinista. Cuando todas las transiciones se encuentran determinadas en una máquina de estados, se tiene una maquina determinista. Si se tiene al menos una transición no definida o indeterminada entonces se tiene una maquina no determinista.

A continuación, un ejemplo de una maquina finita no determinista en dígrafo y su tabla de transición.

![]()

**Figura 3. Diagrama de grafo de una máquina no determinista**

![]()

**Figura 4. Tabla de transición de una máquina no determinista**

(Introducción, Alejandro, & Orozco, n.d.)

**4.2. Máquinas de estado Moore y Mealy**

*4.2.1 Máquina de Mealy*

George Mealy escribió un ensayo en el cual entra en profundidad acerca de crear máquinas de estado desde funciones matemáticas, y describe esas salidas de máquinas de estado en términos de sus entradas. Para diagramar la máquina Mealy, la salida está hecha para depender de ambos: el estado actual y la entrada.

La estructura de una máquina de Mealy es:  

MMe={Q,Ent,Sal,tran,res,qo}

Donde: 

Q: conjunto de estados

Ent: alfabeto de entrada

Sal: alfabeto de salida

tran: función de transición

res: función de respuesta

qo: estado inicial

Gráficamente, se lo representa de la siguiente manera:

![]()

**Figura 5. Esquema explicativo acerca de la máquina de Mealy**

(“Máquinas de Mealy”, n.d.)

(“Máquinas de estado - MCI Capacitación,” n.d.)

*4.2.2 Máquina de Moore*

Edward Moore escribió un ensayo en 1956 titulado Gedanken-experiments on Sequential Machines. En él dice que la salida depende solo del estado, y el próximo estado es dependiente del estado actual y la entrada.

La estructura de una máquina de Moore se lo representa de la siguiente forma: 

MMo = {Q,Ent,Sal,tran,res,qo}

Donde: 

Q: conjunto de estados

Ent: alfabeto de entrada

Sal: alfabeto de salida

tran: función de transición

res: función de respuesta

qo: estado inicial

Gráficamente, se lo representa de la siguiente manera:

![]()

**Figura 6. Esquema explicativo acerca de la máquina de Moore**

Y su tabla sería de la siguiente forma:

![]()

**Figura 5. Tabla de transición de la máquina de Moore**

(“Máquinas de estado - MCI Capacitación,” n.d.)

(“Máquinas de Moore,” n.d.)

**5. DIAGRAMAS**



**Figura 14. Diagrama de bloques del funcionamiento de la calculadora**

**6. LISTA DE COMPONENTES**
- Herramienta de generación de estados de gráfos

**7. MAPA DE VARIABLES**

**8. EXPLICACIÓN DEL CÓDIGO FUENTE**


**9. DESCRIPCIÓN DE PRERREQUISITOS Y CONFIGURACIÓN**

**10. CONCLUSIONES** 

**11. RECOMENDACIONES**

**12. CRONOGRAMA**
![]()

**13. BIBLIOGRAFÍA**
