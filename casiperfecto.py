def perfect_number(numero):
    cont_divisores = 0
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma = suma + i
            cont_divisores = cont_divisores + 1

    suma_divisores = suma
    casi_resta = suma_divisores - numero
    if -3 <= casi_resta <= 3:
        print("El número es casi perfecto")
    else:
        print("El número no es casi perfecto")


numero = int(input("Digite el número"))
perfect_number(numero)