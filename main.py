def menu():
    print("--MENU--")
    print("1. Factorial")
    print("2. Suma N numero naturales")
    print("3. Fibonacci")
    print("4. Contador Letras")
    print("5. Invertir Palabra")
    print("6. Potencia N numero")
    print("7. salir")

def factorial(n):
    if n == 0 :
        return 1
    else:
        print(n)
        return n*factorial(n-1)

def NumeroNatural(numNatural):
    if numNatural == 0 :
        return 1
    else:
        print(numNatural)
        return numNatural+NumeroNatural(numNatural-1)

def Fibonacci(numFibonacci):
    if numFibonacci == 0 or numFibonacci == 1:
        return 1
    else:
        return Fibonacci(numFibonacci - 2) + Fibonacci(numFibonacci - 1)


def Letras(palabra,letra):


    if letra in palabra:
        return palabra.count(letra)


def InvertirPalabra(invertirPalabra):
    if invertirPalabra == []:
        return []

def potencia(base ,exponente):
    if exponente==0:
        return 1
    else:
        return base* exponente(base ,exponente-1)

while True:
    menu()
    op = int(input("\nIngrese la opcion: "))

    match op:
        case 1:
            n= int(input("Ingrese un entero positivo: "))
            print(factorial(n)-1)

        case 2:
            numNatural= int(input("Ingrese un entero positivo: "))
            print(NumeroNatural(numNatural)-1)

        case 3:
            numFibonacci = int(input("Ingrese un entero positivo: "))
            print(Fibonacci(numFibonacci))

        case 4:
            palabra = input("Ingrese un palabra: ").upper()
            print(Letras())
        case 5:
            invertirPalabra = int(input("Ingrese un palabra: ")).upper()

        case 6:
            base = int(input("ingrese la base"))
            exponente = int(input("ingrese la exponente"))
            print(potencia(base,exponente))

        case _:
            print("Opcion no valida")







