#Programa 2

# Para leer los datos
while True:

    # Defino variables
    estado = 0          # El estado se inicia en 0
    entradan = 0
    cont = 0            # Número de díditos de la entrada
    salida = 0

    # Para ingresar los datos
    entrada = input("Ingrese la entrada: ")

    # Transformando la entrada en números
    for i in range(len(entrada)):
        if entrada[len(entrada)-i-1] == 'a':
            entradan = entradan + 1*10**i
        elif entrada[len(entrada)-i-1] == 'b':
            entradan = entradan + 2*10**i
        elif entrada[len(entrada)-i-1] == 'c':
            entradan = entradan + 3*10**i
        else:
            print("Secuencia de entradas incorrectas")
            break
    print(entradan)

    for i in range(len(entrada)):
        digito = entradan % 10
        if estado == 0:
            if digito == 1:
                estado = 0
            elif digito == 2:
                estado = 3
                salida = salida + 1*10**i
            elif digito == 3:
                estado = 2
                salida = salida + 1*10**i
        elif estado == 1:
            if digito == 1:
                estado = 1
            elif digito == 2:
                estado = 1
            elif digito == 3:
                estado = 3
                salida = salida + 1*10**i
        elif estado == 2:
            if digito == 1:
                estado = 1
                salida = salida + 1*10**i
            elif digito == 2:
                estado = 1
                salida = salida + 1*10**i
            elif digito == 3:
                estado = 3
        elif estado == 3:
            if digito == 1:
                estado = 2
                salida = salida + 1*10**i
            elif digito == 2:
                estado = 3
            elif digito == 3:
                estado = 0 
                salida = salida + 1*10**i
        entradan = int(entradan / 10)
    print("La salida es: ",salida)
