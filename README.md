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

*4.1.1. Máquinas Finitas Determinísticas*

Los circuitos sumadores son circuitos muy utilizados en distintos tipos de sistemas digitales. Para comprender efectivamente el funcionamiento de un circuito sumador, primero se debe entender el funcionamiento de un semisumador. El semisumador realiza únicamente la suma de dos números binarios con un bit cada uno. 

![](https://github.com/aledomesalazar/Producto-de-Unidad_Segundo-Parcial/blob/master/img/WhatsApp%20Image%202020-08-04%20at%2013.26.14.jpeg)

**Figura 1. Diagrama de bloque de un circuito semisumador**


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
