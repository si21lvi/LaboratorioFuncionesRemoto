def perfect_number(numero):
    cont_divisores = 0
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma = suma + i
            cont_divisores = cont_divisores + 1

    suma_divisores = suma
    if numero == suma_divisores:
        print("El número es perfecto")
    else:
        print("El número no es perfecto")


numero = int(input("Digite el número"))
perfect_number(numero)