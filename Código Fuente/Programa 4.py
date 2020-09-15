#Programa 3

# Para leer los datos
while True:

    # Defino variables
    estado = 'S'        # El estado se inicia en S
    cont = 0            # Número de dígitos de la entrada
    salida = 0          # Inicializa la salida con 0

    # Para ingresar los datos
    entrada = int(input("Ingrese la entrada: "))
    
    # Para validar los dígitos
    digito = 0
    validar = entrada
    while cont <4:
        digito = validar % 10
        if (digito !=0 and digito !=1):
            print("Secuencia de entradas incorrectas")
            break
        validar = int(validar / 10)
        cont = cont + 1

    # Establece el orden correcto
    digito = 0
    orden = entrada
    aux = 0
    for i in range(4):
        digito = orden % 10
        aux = aux + digito*10**(4-i-1)
        orden = int(orden / 10)
    entrada = aux

    # Simulando la máquina de estados
    i = 0
    while (i != 4 and salida == 0):
        digito = entrada % 10
        if (estado == 'S'):
            if digito == 0:
                estado = 'V'
            elif digito == 1:
                estado = 'S'
                salida = 2
        elif (estado == 'V'):
            if digito == 0:
                estado = 'R'
            elif digito == 1:
                estado = 'V'
                salida = 2
        elif (estado == 'R'):
            if digito == 0:
                estado = 'R'
                salida = 1
            elif digito == 1:
                estado = 'D'
        elif (estado == 'D'):
            if digito == 0:
                estado = 'D'
                salida = 1
            elif digito == 1:
                estado = 'D'
        entrada = int(entrada/10)
        i = i+1

    # Muestra el resultado
    if salida == 1:
        print("La bomba se activa")
    else:
        print("La bomba no se activa")
