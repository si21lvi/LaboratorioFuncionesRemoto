def a_power_b(a, b):
    cont = 1
    for i in range(0, b):
        cont = cont * a
    return cont


x = int(input("Ingrese un número"))
y = int(input("Ingrese el numero "))

ac = a_power_b(x, y)
print(ac)