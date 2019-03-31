def is_prime(a):
    contador = 0

    for i in range(1, a + 1):
        if a % i == 0:
            contador += 1

    if contador == 2:
        return 1

    else:
        return 0


contarprimo = 0
cont_primo = 0
while True:

    try:

        x = int(input("Ingrese un numero"))

        cd = is_prime(x)
        if cd == 1:
            contarprimo += 1
            cont_primo += 1

        cdp = is_prime(cont_primo)
        if cdp == 1:
            x1 = ("el numero de veces es primo")
        if cdp == 0:
            x1 = ("el numero de veces no es primo")
        if x <= 0:
            print("-1")
            print("No se puede determinar y se calcularon:", contarprimo, "primos y", x1)
            break

        print(cd)

    except ValueError:
        print("-1")
        print("No se permite ingresar letras y se calcularon:", contarprimo, "primos y", x1)