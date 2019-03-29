def a_power_b(a, b):
    cont = 1

    for i in range(0, b):
        cont = cont * a

    return cont


while True:

    x = int(input("Ingrese la base "))

    if x == 0:
        print("Nos vemos!")
        break

    y = int(input("Ingrese el exponente "))
    ac = a_power_b(x, y)
    print(ac)
