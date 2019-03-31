def is_prime(s):
    cont = 0
    for i in range(1, s + 1):
        if s % i == 0:
            cont += 1

    if cont == 2:
        return 1
    else:
        return 0


while True:

    try:

        x = int(input("Digite un numero"))
        if x == 0:
            print("No se puede determinar")
            print(-1)
            break

        t = is_prime(x)
        print(t)

    except ValueError:
        print("-1")
        print("No se permiten letras")