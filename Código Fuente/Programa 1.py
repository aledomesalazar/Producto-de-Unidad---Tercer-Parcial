#Programa 1

# Para leer los datos
while True:

    # Defino variables
    estado = 0          # El estado se inicia en 0
    cont = 0            # Número de díditos de la entrada
    salida = 0

    # Para ingresar los datos
    entrada = int(input("Ingrese la entrada: "))

    # Para validar los dígitos
    digito = 0
    validar = entrada
    while validar != 0:
        digito = validar % 10
        if (digito !=0 and digito !=1):
            print("Secuencia de entradas incorrectas")
            break
        validar = int(validar / 10)
        cont = cont + 1

    print(entrada)

    for i in range(cont):
        digito = entrada % 10
        if estado == 0:
            if digito == 0:
                estado = 0
                salida = salida + 1*10**i
            elif digito == 1:
                estado = 4
                salida = salida + 1*10**i
        elif estado == 1:
            if digito == 0:
                estado = 0
            elif digito == 1:
                estado = 3
                salida = salida + 1*10**i
        elif estado == 2:
            if digito == 0:
                estado = 0
            elif digito == 1:
                estado = 2
        elif estado == 3:
            if digito == 0:
                estado = 1
                salida = salida + 1*10**i
            elif digito == 1:
                estado = 1
                salida = salida + 1*10**i
        elif estado == 4:
            if digito == 0:
                estado = 1
                salida = salida + 1*10**i
            elif digito == 1:
                estado = 1
        entrada = int(entrada / 10)
    print("La salida es: ",salida)
