


def crearMenu():
    print("1.calcular cuadrado")
    print("2.calcular triangulo")
    print("3.calcular cirdulo")
    print("4.salir")
    print("elixa opcion")


def calcularAreaCuadrado(base, altura):
        area = base * altura

        return area


def calcularAreaCirculo(r):
    area = 3.14 * r * r

    return area


def calcularAreaTriangulo(base, altura):
    area = base * altura / 2
    return area


def RecollerParametros(opcion):
    if opcion == 1 or opcion == 2:
        base = float(input('digite um numero para la base: '))
        altura = float(input('digite um numero para la altura: '))
        return (base, altura)
    elif opcion == 3:
        radio = float(input('digite um numero para el radio: '))
        return (radio)
def exercicioBoletin4_2 ():
    opcion = 0
    while opcion != 4:
        crearMenu()
        opcion = int(input("Escribe una opcion: "))
        if opcion >0 and opcion < 5:
            if opcion == 1 or opcion == 2:
                base, altura = RecollerParametros(opcion)
                if opcion == 1:
                    area = calcularAreaCuadrado(base, altura)
                    print("el area del cadrado es: ", area)
                if opcion == 2:
                    area = calcularAreaTriangulo(base, altura)
                    print("el area del triangulo es: ", area)
            elif opcion == 3:
                    radio = RecollerParametros(opcion)
                    area = calcularAreaCirculo(radio)
                    print("el area del circulo es: ",area)

exercicioBoletin4_2()