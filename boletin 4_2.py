def calcularArea():
    print("que figura elijes")
    print("1. cadrado")
    print("2. circulo")
    print("3. triangulo")
    float(input('digite um numero: '))
    return int(input('digite um numero: '))

calcularArea()




def calcularAreaCuadrado(base,altura):
        area = base*altura

        return area
def calcularAreaCirculo(r):
        area = 3,14*r*r

        return area

def calcularAreaTriangulo(base,altura):

        area = base*altura/2

        return area



def crearMenu():
    print("que figura elijes")
    print("1. cadrado")
    print("2. triangulo")
    print("3. circulo")
    return int(input())
crearMenu()

