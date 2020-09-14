# Producto de Unidad - Tercer Parcial
## Aplicación de la máquina de estados en problemas reales

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

![](https://github.com/aledomesalazar/Producto-de-Unidad---Tercer-Parcial/blob/master/img/WhatsApp%20Image%202020-09-14%20at%2010.52.18.jpeg)

**Figura 1. Diagrama de transición o dígrafo**

En un diagrama de transición existe un nodo por cada estado de Q. Los estados finales están encerrados en un círculo doble. El estado inicial es apuntado por una flecha que no proviene de ningún otro estado. Para cada estado hay exactamente una y sólo una flecha que inicia en un estado y termina en otro estado.

Para describir por completo una función de transición se ocupa una Tabla de Transición. Las columnas se etiquetan con los símbolos de entrada; las filas son etiquetadas con los estados y en las intersecciones se colocan los nuevos estados, como se muestra en la figura a continuación. 

![](https://github.com/aledomesalazar/Producto-de-Unidad---Tercer-Parcial/blob/master/img/WhatsApp%20Image%202020-09-14%20at%2010.52.23.jpeg)

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

![](https://github.com/aledomesalazar/Producto-de-Unidad---Tercer-Parcial/blob/master/img/WhatsApp%20Image%202020-09-14%20at%2010.52.33.jpeg)

**Figura 3. Diagrama de grafo de una máquina no determinista**

![](https://github.com/aledomesalazar/Producto-de-Unidad---Tercer-Parcial/blob/master/img/WhatsApp%20Image%202020-09-14%20at%2010.52.39.jpeg)

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

![](https://github.com/aledomesalazar/Producto-de-Unidad---Tercer-Parcial/blob/master/img/WhatsApp%20Image%202020-09-14%20at%2010.52.45.jpeg)

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

![](https://github.com/aledomesalazar/Producto-de-Unidad---Tercer-Parcial/blob/master/img/WhatsApp%20Image%202020-09-14%20at%2010.52.50.jpeg)

**Figura 6. Esquema explicativo acerca de la máquina de Moore**

Y su tabla sería de la siguiente forma:

![](https://github.com/aledomesalazar/Producto-de-Unidad---Tercer-Parcial/blob/master/img/WhatsApp%20Image%202020-09-14%20at%2010.52.53.jpeg)

**Figura 7. Tabla de transición de la máquina de Moore**

(“Máquinas de estado - MCI Capacitación,” n.d.)

(“Máquinas de Moore,” n.d.)

**5. EXPLICACIÓN DEL CÓDIGO FUENTE**

*5.1 1.	Dibuje el diagrama de estados para la máquina de estado finito cuya tabla de estados es la siguiente. Partiendo del estado s0, calcula la salida para la cadena de entrada 1000110.*

![](https://github.com/aledomesalazar/Producto-de-Unidad---Tercer-Parcial/blob/master/img/WhatsApp%20Image%202020-09-14%20at%2010.53.07.jpeg)

**Figura 8. Tabla de transición del ejercicio 1**

La lectura de la tabla empieza con el primer estado que tiene la tabla, en este caso S0, y continua la lectura de izquierda a derecha. 

Cuando la entrada es 0 en estado S0, el siguiente estado es S0; esto quiere decir que se queda en el mismo estado y para ver el valor de la salida, se ve observa de igual forma el valor de la entrada. Para el estado S0 cuando la entrada es 0 la salida será 1. Ahora se observa la entrada 1, con este valor de entrada el estado siguiente es S4 y la salida será 1. Cuando se terminan los valores de entrada se termina las transiciones del estado y se pasa al siguiente.

Para el estado S1 cuando la entrada es 0 el estado siguiente será S0 y la salida será 0. Cuando el valor de la entrada es 1 el estado siguiente será S3 y la salida tendrá el valor de 1. Con la entrada 0 en estado S2 el siguiente estado será S0 y su salida será 0, mientras que para la entrada 1 el estado siguiente será S2 (se mantiene en el mismo estado) y su salida será 0. Para el estado S3 se tiene que con ambos valores de entrada (0 y 1) su siguiente estado será S1 y sus salidas con ambos valores de entrada será 1. Para el ultimo estado S4 cuando el valor de entrada es 0 su siguiente estado será S1 y el valor de su salida será 1 y por último con un valor de entrada de 1 su siguiente estado será S0 y su salida será 0. 

![](https://github.com/aledomesalazar/Producto-de-Unidad---Tercer-Parcial/blob/master/img/WhatsApp%20Image%202020-09-14%20at%2010.53.24.jpeg)

**Figura 9. Grafo de estados del ejercicio 1**

Una vez obtenido el grafo de estados, el problema dice que a la entrada S0 se ingresa 100110 y pide su salida. Para obtener el valor de salida de la cadena de entrada primero de empieza con el bit menos significativo y se continua de derecha a izquierda hasta el bit más significativo. El bit menos significativo es 0 viendo el diagrama de estados cuando se ingresa un 0 en el estado S0 este se mantiene en el mismo estado y su salida es 1, por ende 1 será el bit menos significativo del resultado. 

El siguiente valor de la entrada es el 1 en estado S0 (esto por la entrada anterior) se observa de nuevo el diagrama de estados. Cuando se ingresa 1 en estado S0 su siguiente estado es S4 y su salida será 1. Del resultado se tiene 11. El siguiente valor de la entrada es 1 en el estado S4 (esto por la entrada anterior), observando el diagrama de estados se tiene que con este valor de entrada su siguiente estado es S0 y su salida será 0, dando el resultado 011. Ahora en la entrada se tiene el valor de 0 en estado S0 (este estado por la entrada anterior), observando el diagrama con el valor de entrada 0 en S0, la maquina se mantiene en el mismo estado y la salida es 1, dando un resultado de 1011. El proceso anterior se repite con las siguientes dos entradas dando un resultado de 11011. Para el bit más significativo el estado cambia al estado S4, debido a que el valor de entrada es 1 y su salida será 1, dando como resultado final 111011 de la entrada 1000110. 

![](https://github.com/aledomesalazar/Producto-de-Unidad---Tercer-Parcial/blob/master/img/WhatsApp%20Image%202020-09-14%20at%2010.53.32.jpeg)

**Figura 10. Tabla que describe cada uno de los resultados y la salida acumulada a partir de la entrada 1000110**

*5.1 2.	Dibuje el diagrama de estados para la máquina de estado finito cuya tabla de estados es la siguiente. Partiendo del estado inicial s0, calcula la salida para la cadena de entrada abbccc.*

![](https://github.com/aledomesalazar/Producto-de-Unidad---Tercer-Parcial/blob/master/img/WhatsApp%20Image%202020-09-14%20at%2010.53.40.jpeg)

**Figura 12. Tabla de transición del ejercicio 2**

Para realizar el diagrama de estados primero se empieza con el estado S0, cuando la entrada en estado tiene el valor de “a” se mantiene en el mismo estado y su salida será 0. En estado S0 cuando la entrada es “b” su siguiente estado será S3 y su salida será 1 y por ultimó con la entrada “c” su siguiente estado es S3 y su salida será 1. 
Para el estado S1 con las entradas “a” y “b” se mantiene en el mismo estado y sus salidas tendrán el valor de 0 para ambas entradas. En el mismo estado con una entrada de “c” su estado siguiente será S3 y su salida será 1. 

Para el estado S2 con las entradas “a” y “b” se produce un cambio de estado al estado S1 y sus salidas tendrán el valor de 1 para ambas entradas. En el mismo estado con una entrada de “c” su estado siguiente será S3 y su salida será 0. 

Para el ultimo estado S3 cuando el valor de entrada es “a” su siguiente estado será S2 y su salida será 1. Con un valor de entrada “b” se mantiene en el mismo estado y su salida será 0. Y con valor de entrada “c” en estado S3 su estado siguiente será S0 y su salida será 1. 

![](https://github.com/aledomesalazar/Producto-de-Unidad---Tercer-Parcial/blob/master/img/WhatsApp%20Image%202020-09-14%20at%2010.53.50.jpeg)

**Figura 13. Grafo de estados del ejercicio 2**

Una vez obtenido el grafo de estados, el problema dice que a la entrada S0 se ingresa abbccc y pide su salida. Para resolver este problema se empieza con el bit menos significativo y se continua de derecha a izquierda hasta el bit más significativo. El bit menos significativo es “c” en estado S0, este valor de entrada cambia al estado S2 y da a la salida el valor de 1. La siguiente entrada es “c” en estado S2, este valor provoca un cambio al estado S3 y una salida de 0. Con la entrada “c” en estado S3 se cambia al estado S0 y se tendrá una salida de 1. Con una entrada de “b” en estado S0 se regresa al estado S3 obteniendo una salida de 1. Con el valor de “b” como entrada en el estado S3 se mantiene en el mismo estado y se obtiene en la salida el valor de 0. Por último, con la entrada “a” (bit más significativo) en estado S3 se produce un cambio de estado al estado S2 y una salida de 1. Se obtiene como resultado final 101101 de la entrada abbccc.

![](https://github.com/aledomesalazar/Producto-de-Unidad---Tercer-Parcial/blob/master/img/WhatsApp%20Image%202020-09-14%20at%2010.54.01.jpeg)

**Figura 14. Tabla que describe cada uno de los resultados y la salida acumulada a partir de la entrada abbccc**

*5.1 3. Halle la tabla de estados para la máquina de estado finito cuyo diagrama de estados es:*

![](https://github.com/aledomesalazar/Producto-de-Unidad---Tercer-Parcial/blob/master/img/WhatsApp%20Image%202020-09-14%20at%2010.54.11.jpeg)

**Figura 15. Tabla de transición del ejercicio 3**

Para obtener la tabla de transiciones del diagrama de estados primero se debe visualizar cuales son todos los estados, también cuales son los valores de entrada y la salida que se produce con ese valor de entrada. Los números que se encuentran en la parte superior de cada una de las flechas representan el valor de la entrada y el valor de la salida respectivamente. La dirección de cada una de las flechas indica cuál es el estado siguiente. 

Se empieza con la entrada 0 en el estado S0, se observa que la flecha de apunta al estado S1 posee los valores de 0,1 donde se interpreta que cuando existe una entrada de 0 en el estado S0 su estado siguiente será el estado S1 y su salida será 1. Con el valor de entrada 1 en estado S0 se observa la flecha en dirección al estado S3, esta flecha posee los valores 1,0 lo que indica que el estado siguiente de S0 cuando el valor de entrada es 1 será S3 y su salida será 0. 

Se pasa al estado S1 de igual forma se comienza con la entrada 0, se observa que con ese valor de entrada la dirección de la flecha apunta al estado S0. Esta flecha posee los valores 0,1 que indica que con un valor de entrada de 0 en estado S1 su siguiente estado será S0 y su salida será 1. Cuando se ingresa un valor de 1 en el estado S1 se observa que la dirección de la flecha apunta al estado S2, donde la flecha posee los valores 1,0. Lo que indica que cuando la entrada sea 1 en estado S1 su siguiente estado será S2 y su salida será 0. 

Se pasa al estado S2 y una entrada de 0, se observa que la dirección de la flecha apunta al estado S1 donde posee los valores 0,1; esto indica que en una entrada de 0 en el estado S2 su siguiente estado será S1 y su salida será 1. Con la entrada de 1 se puede observar que la flecha apunta al estado S3 que posee los valores 1,1, lo cual indica que para una entrada de 1 en el estado S2 su siguiente estado será S3 y su salida será 1. 

Por último, queda el estado S3 donde se empieza con el valor de 0, se puede apreciar que la dirección de la flecha apunta al estado S2, esta flecha posee los valores 0,0 lo que indica que para un valor de entrada de 0 en estado S3 su siguiente estado será S2 y su salida será 0. Para el valor de entrada 1 en estado S3 se observa que la flecha apunta al estado S0, donde se tiene los valores 1,0. Esto indica que en una entrada de 1 en el estado S3 su siguiente estado será S0 y su salida será 0. 

Comprendida toda la información del diagrama de estados se procede a llenar la tabla de transiciones. La tabla se encuentra constituida por los estados que conforman la primera columna, la transición que ocupa la segunda columna y la salida que ocupa la columna final. Tanto en la columna de transición como la de salida debe ir los valores de la entrada (0,1). 

![](https://github.com/aledomesalazar/Producto-de-Unidad---Tercer-Parcial/blob/master/img/WhatsApp%20Image%202020-09-14%20at%2010.54.20.jpeg)

**Figura 16.Diagrama de grafos, resultado del ejercicio 3**

*5.1 4. Construya una máquina de estado finito que modele una máquina expendedora de bebidas que acepta monedas de 5, 10 y 20 centavos. La máquina acepta monedas hasta que se introducen 25 centavos y devuelve cualquier cantidad que supere los 25 centavos. Entonces, el cliente puede pulsar los botones y elegir una bebida de cola (C), cerveza (Z) o agua (A).*

Para construir una máquina de estado se debe tener la siguiente información: el número de entradas, el número de salidas, el número de estados, la tabla de verdad de las salidas y la tabla de verdad de los estados siguientes. El problema dice que la máquina expendedora acepta los valores de 5, 10 y 20 centavos; cuándo se ingresa un valor de 25 centavos la maquina devolverá cualquier valor mayor a los 25 centavos ingresados y una bebida a su selección entra Cola (C), Cerveza (Z) y Agua (A). 

Las entradas para la máquina de estado son 5,10, 20, C, Z y A. Se tiene 8 posibles estados. Las salidas dependerán de la acumulación que se dé durante el procedimiento de funcionamiento de la máquina de estados. Las tablas de igual forma dependen de la forma en la que se construye la máquina de estados.

Cuando al estado S0 se le ingresa el valor de entrada 5 pasa al siguiente estado y su salida será Cola (C), cuando se ingresa un valor de 10 su siguiente estado será S2 y su salida será Cola (C). Para el ingreso del valor 20 su siguiente estado será S5 y su salida será nula (N). Cuando se ingresa los valores C, Z y A al estado S0 este se mantendrá en el mismo estado y sus salidas serán nulas (N).

Con el estado S1 se aplica el mismo procedimiento del estado S0. Cuando se ingresa el valor de 5 este cambia de estado al S2 y su salida será C, en la entrada 10 se cambia de estado al S3 y su salida será C; con la entrada 20 se cambia al estado S6 y su salida será nula (N). Con las entradas C, Z y A se mantiene en el mismo estado y sus salidas serán nulas (N). 

Con estado S2 y S3 se tiene que cuando la entrada es 5 y 10 se cambian a los estados S3, S4 y S4, S5 respectivamente y sus salidas serán iguales a C. Para la entrada de 20 se obtiene que para el estado S2 se cambia al estado S6 y su salida será nula (N); en cambio, para el estado S3 se cambia al estado S7, pero su salida será de 5 esto se debe a la acumulación de los valores anteriores ingresados en la máquina de estados. Para ambos estados (S2 y S3) con las entradas C, Z y A se mantienen en el mismo estado y sus salidas serán nulas (N). 

Con los estados S4 y S5 se debe tener en consideración que para la entrada 20 su valor será el acumulado de los estados anteriores. Para las entradas 5 y 10 la mecánica es la misma al igual que sus salidas serán las mismas. Cuando el valor es de 20 para el estado S4 su siguiente estado será S7 y su salida será 10; en cambio para el estado S5 con la misma entrada su siguiente estado será S7 y su salida será 15. Para las entradas C, Z y A se mantiene en el mismo estado y sus salidas serán nulas (N).

Para el estado S6 las entradas 5, 10 y 20 se van al estado S7 y sus salidas serán C, 5 (este valor de 5 es por la acumulación de los estados anteriores) y 20 respectivamente. Con las entradas C, Z y A se mantiene en el mismo estado y sus salidas serán nulas (N). Por último, se tiene el estado S7 donde las entradas 5, 10, 20 hacen que la máquina se mantenga en el mismo estado y sus salidas serán 5, 10, 15 respectivamente; esto debido a la acumulación de los estados anteriores. Como este es el estado final la acumulación es la máxima posible por ende cuando se dan las entradas C, Z y A estas pasan a ser estados también de tal manera que con cada entrada su estado siguiente será su mismo valor de entrada; lo mismo aplica para la salida. 

![](https://github.com/aledomesalazar/Producto-de-Unidad---Tercer-Parcial/blob/master/img/WhatsApp%20Image%202020-09-14%20at%2010.54.33.jpeg)

**Figura 17. Diagrama de grafos, resultado del ejercicio 4**

![](https://github.com/aledomesalazar/Producto-de-Unidad---Tercer-Parcial/blob/master/img/WhatsApp%20Image%202020-09-14%20at%2010.54.27.jpeg)

**Figura 18. Tabla de transiciones, resultado del ejercicio 4**

*5.1.5.	Construya una máquina de estados finito que modele un circuito de riego automático como el mostrado en la figura. El circuito deberá accionar la bomba en las siguientes condiciones:*

a) *El circuito accionará la bomba solamente cuando la tierra esté seca, pero antes debe comprobar las siguientes condiciones:*

*- i. Para evitar que la bomba se estropee por funcionar en vacío, nunca se accionará la bomba cuando el depósito de agua esté vacío.* 

*- ii. Si hay restricciones en el riego (época de verano), sólo se podrá regar de noche.*

*- iii. En el resto del año (si no hay restricciones) se podrá regar de día y de noche (si la tierra está seca).*

b) *Para la implementación del circuito se dispone de las siguientes entradas:* 

*- i. S: Señal que indica si la tierra está seca: Tierra seca: S=1; Tierra húmeda: S=0*

*- ii. R: Señal que indica si hay restricciones en el riego (es verano): Hay restricciones: R=1 No hay restricciones: R=0* 

*- iii. D: Señal que indica si es de día o de noche: Día: D=1; Noche: D=0*

*- iv. V: Señal que indica si el depósito de agua está vacío: Vacío: V=1; Hay agua: V=0*

c) *Y la salida B, que accionará la bomba para regar: Bomba funcionando: B=1; Bomba apagada B=0.*

Para la construcción de la máquina de estados que permita el riego automático se toma en consideración únicamente los valores en los cuales las condiciones se cumplen para que la bomba funcione (B=1). Para que esto funcione, primero se debe verificar que la tierra se encuentre seca (S=1), esto provoca que se cambie a la siguiente validación o que se compruebe la siguiente condición, pero su salida B tendrá el valor de cero porque no sean comprobado todas las condiciones para que esta funcione. En el caso de que la tierra se encuentre húmeda (S=1), entonces la maquina se mantiene sin hacer ningún cambio y su salida B tendrá el valor de 0.

De ahí sigue la siguiente validación que es comprobar el estado del tanque. Si el tanque se encuentra vacío (V=1), entonces no se produce ningún cambio en la máquina y la salida B tendrá el valor de 0. En cambio, cuando el tanque se encuentra lleno (V=0) se produce un cambio hacia la siguiente validación y la salida B tendrá el valor de 0, esto por la misma razón que con el caso anterior no sean validado todas las condiciones para que la bomba funcione. 

Una vez comprobado que el tanque se encuentra vacío, se comprueba que no haya restricciones. Las restricciones vienen a representar las estaciones del año, en la estación de verano se regará únicamente en la noche, esa es la restricción. Por lo tanto, cuando haya restricciones (R=1), entonces se considera el momento del día en que se vaya a regar; caso contrario (R=0) el momento se desprecia y la salida B será 1. En las restricciones se considera el momento del día como se dijo anteriormente, si es de día (D=1), entonces la salida B será de 0, porque la restricción limita que el riego sea por las noches; caso contrario (D=0) la salida será 1.

![](https://github.com/aledomesalazar/Producto-de-Unidad---Tercer-Parcial/blob/master/img/WhatsApp%20Image%202020-09-14%20at%2010.54.43.jpeg)

**Figura 19. Diagrama de grafos, resultado del ejercicio 5**

![](https://github.com/aledomesalazar/Producto-de-Unidad---Tercer-Parcial/blob/master/img/WhatsApp%20Image%202020-09-14%20at%2010.54.51.jpeg)

**Figura 20. Tabla de transiciones, resultado del ejercicio 5**

**6. DESCRIPCIÓN DE PRERREQUISITOS Y CONFIGURACIÓN**

Para esta actividad no es obligatorio la implemetación de un software específico. Sin embargo, se uso la siguiente página para la construcción de los grafos de estado.

- (Pendiente la página)

**7. CONCLUSIONES** 

1.	Se concluye que mediante la precedencia de una tabla de transiciones se construye los grafos de estados y se lo puede establecer de forma inversa. 
2.	La máquina de estados llega a ser una representación, donde establece si un suceso depende o no de un estado anterior, siendo que las entradas y salidas pueden manejarse con decisiones duales, si o no, o añadir un resultado específico diferente a ellos.
3.	En la mayoría de aplicaciones, se utiliza las representaciones de Mealy ya que las transiciones y las salidas dependían de las entradas y los estados que se encontraban.

**8. RECOMENDACIONES**

1.	Se recomienda usar diagramas de grafos debido a que es más dinámico y entendible representar con 5 estados, a partir de 6 en adelante es más recomendable representar por las tablas ya que lo generaliza.
2.	Simular estos problemas es muy útil para el desarrollo de la lógica de programación, siendo que mayoría de estos manejan varios if. También es aplicable para circuitos digitales ya que en su mayoría manejan dos estados: verdadero o falso.
3.	La representación de estados es un inicio para introducir al mundo de la inteligencia artificial ya que cada estado puede ser dependiente del otro o ser independiente, puede inicializarse o no y del mismo puede derivarse en uno o más estados, sirviendo para mejor organización en la toma de decisiones.


**9. CRONOGRAMA**

![](https://github.com/aledomesalazar/Producto-de-Unidad---Tercer-Parcial/blob/master/img/WhatsApp%20Image%202020-09-14%20at%2013.51.45.jpeg)

**10. BIBLIOGRAFÍA**

- Babakov, R., & Barkalov, A. (2018). Structural representation of synthesis methods of finite state machine with datapath of transitions. Proceedings of 2018 IEEE 9th International Conference on Dependable Systems, Services and Technologies, DESSERT 2018, 229–233. https://doi.org/10.1109/DESSERT.2018.8409134
- Introducción, B., Alejandro, J., & Orozco, G. (n.d.). Máquinas de Estados Finitos.
- Kinoshita, Y., Hosokawa, T., & Fujiwara, H. (2019). A Test Generation Method Based on k-Cycle Testing for Finite State Machines. 2019 IEEE 25th International Symposium on On-Line Testing and Robust System Design, IOLTS 2019, 232–235. https://doi.org/10.1109/IOLTS.2019.8854426
- Máquinas de estado - MCI Capacitación. (n.d.). Retrieved September 5, 2020, from https://cursos.mcielectronics.cl/2019/06/18/maquinas-de-estado/
- Máquinas de Mealy. (n.d.). Retrieved September 5, 2020, from http://delta.cs.cinvestav.mx/~gmorales/ta/node49.html
- Máquinas de Moore. (n.d.). Retrieved September 5, 2020, from http://delta.cs.cinvestav.mx/~gmorales/ta/node50.html
- Smolyakov, I. Y., & Belyaev, S. A. (2019). Design of the software architecture for starcraft video game on the basis of finite state machines. Proceedings of the 2019 IEEE Conference of Russian Young Researchers in Electrical and Electronic Engineering, ElConRus 2019, 356–359. https://doi.org/10.1109/EIConRus.2019.8656866

**11. ANEXOS**

*11.1 Manual de Usuario*

*11.1.1 ¿Cómo realizar los diagramas de estados?*

Para empezar a realizar bien los diagramas de estados de los problemas 1 y 2, primero se debe saber cómo leer bien la tabla. 

![](https://github.com/aledomesalazar/Producto-de-Unidad---Tercer-Parcial/blob/master/img/WhatsApp%20Image%202020-09-14%20at%2010.55.05.jpeg)

**Figura 21. Tabla de transición**

Donde se encuentra la flecha roja se empieza a leer la tabla de transiciones. En este caso se empieza con el estado S0, luego se lee la flecha de color verde que indica el valor 0 de la entrada. A continuación, se lee la flecha de color azul que indica el estado siguiente, en este caso S0. Por último, se lee la flecha de color negro que indica el valor de la salida que tiene el estado con ese valor de entrada. La interpretación es la siguiente:

“En el estado S0 cuando la entrada tiene el valor de 0 su siguiente estado será S0 y su salida será 1.”

Ahora en el diagrama primero se debe colocar el estado de inicio donde de un círculo. En este caso el estado de inicio es S0. Quedando de la siguiente forma:

![](https://github.com/aledomesalazar/Producto-de-Unidad---Tercer-Parcial/blob/master/img/WhatsApp%20Image%202020-09-14%20at%2010.55.12.jpeg)

**Figura 22. Representación de un estado**

A continuación, se colocan la flecha que apunta al estado siguiente, en este caso es una retroalimentación por lo tanto la flecha apunta al mismo estado, como se muestra en la siguiente figura.

![](https://github.com/aledomesalazar/Producto-de-Unidad---Tercer-Parcial/blob/master/img/WhatsApp%20Image%202020-09-14%20at%2010.55.16.jpeg)

**Figura 23. Representación de un estado donde su transición devuelve a la misma**

Se colocan los valores de entrada y de salida encima del cuerpo de la flecha de la siguiente forma 0,1. El 0 representa el valor de entrada y el 1 representa el valor de salida. 

![](https://github.com/aledomesalazar/Producto-de-Unidad---Tercer-Parcial/blob/master/img/WhatsApp%20Image%202020-09-14%20at%2010.55.20.jpeg)

**Figura 24. Representación de un estado con su flecha de transición representado por su entrada y salida**

Ahora con el valor de entrada 1 se realiza el mismo procedimiento. Quedando la interpretación de la siguiente forma: 

“En el estado S0 cuando la entrada tiene el valor de 1 su siguiente estado será S4 y su salida será 1.”

Para su implementación en el diagrama de estados se realiza el mismo procedimiento descrito anteriormente, quedando el diagrama de la siguiente manera.

![](https://github.com/aledomesalazar/Producto-de-Unidad---Tercer-Parcial/blob/master/img/WhatsApp%20Image%202020-09-14%20at%2010.55.25.jpeg)

**Figura 25. Representación de dos estados, donde uno tiene dos transiciones**

Una vez acabado el primer estado de la tabla de transiciones se realiza el mismo procedimiento con los demás estados de la tabla.

*11.1.2 ¿Cómo realizar la tabla de transiciones?*

En el problema 3 pide realizar la tabla de transiciones, partiendo del diagrama de estados. Para realizar la tabla primero se deben identificar el número de estados, el número de entradas y el número de salidas. 

![](https://github.com/aledomesalazar/Producto-de-Unidad---Tercer-Parcial/blob/master/img/WhatsApp%20Image%202020-09-14%20at%2010.55.31.jpeg)

**Figura 26. Diagrama de estados, donde señala la transición de S0 a S1**

En el anterior diagrama se puede observar que hay cuatro estados (S0, S1, S2, S3), dos valores de entrada (0,1) y dos valores de salida (0,1). Se empieza con el estado inicial, en este caso es S0, y se toma como referencia el valor de entrada 0. Se identifica la flecha que posee el valor de 0 en la entrada, en este caso el cuadro de color rojo indica los valores de la flecha a los que la entrada es 0 en estado S0. La dirección de la flecha apunta al estado S1 y el otro número a lado del cero indica la salida, por tanta, cuando hay un 0 en la entrada en el estado S0 su siguiente estado será S1 y su salida será 1. 

La construcción de la tabla debe cumplir con los siguientes aspectos: 
1.	En la primera columna deben ir los estados. 
2.	En la columna siguiente las transiciones.
3.	En la columna siguiente las salidas.
4.	Debajo de las transiciones y de las salidas debe ir las entradas con sus respectivos valores.

La tabla quedaría de la siguiente forma:

![](https://github.com/aledomesalazar/Producto-de-Unidad---Tercer-Parcial/blob/master/img/WhatsApp%20Image%202020-09-14%20at%2010.55.38.jpeg)

**Figura 27. Tabla de transición, donde señala las celdas de una entrada **

Para llevar la tabla primero se debe ir con el primer estado que se encuentra señalado con la flecha roja. Luego con el primer valor de entrada el que se encuentra señalado con la flecha en verde. En el diagrama se observó que con una entrada de 0 en el estado S0 su siguiente estado será S1, este dato se debe poner en la casilla donde apunta la flecha azul y el valor de la salida, en este caso 1, debe ir anotado en la casilla que apunta la flecha color negro. 

Quedando de la siguiente forma:

![](https://github.com/aledomesalazar/Producto-de-Unidad---Tercer-Parcial/blob/master/img/WhatsApp%20Image%202020-09-14%20at%2010.55.42.jpeg)

**Figura 28. Tabla de transición, donde señala el dato de una entrada y el correspondiente resultado de la salida**

Se realiza el mismo procedimiento con el valor de entrada 1 en el estado S0. 

![](https://github.com/aledomesalazar/Producto-de-Unidad---Tercer-Parcial/blob/master/img/WhatsApp%20Image%202020-09-14%20at%2010.55.53.jpeg)

**Figura 29. Diagrama de estados, donde señala la transición de S0 a S3**

Los datos de la entrada 1 en el estado S0 se encuentran encerrados en el cuadro verde. La dirección apunta al estado S4 y el otro número que se encuentra a lado del 1 es el valor de la salida. Se interpreta que en la entrada 1 en el estado S0 su siguiente estado es S4 y su salida es 0. 

Para llevar la tabla se realiza el procedimiento antes descrito para la entrada 0, quedando la tabla de la siguiente forma

![](https://github.com/aledomesalazar/Producto-de-Unidad---Tercer-Parcial/blob/master/img/WhatsApp%20Image%202020-09-14%20at%2010.55.59.jpeg)

**Figura 30. DTabla de transición, donde señala otro  dato de las entradsa y el correspondiente resultado de la salida**

Una vez finalizado el primer estado se procede a realizar el mismo procedimiento con el resto de estados hasta llevar la tabla de transiciones.
