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
    num = 0
    numAnterio = 0
    if numFibonacci == num :
        return 1
    else:
        num+=1
        numAnterio = Fibonacci()
        return

def Letras(palabra,letra):

    cont = 0
    contadorLetras = 0
    if cont == contadorLetras:
        return 1
    else:
        for Letra in palabra:
            if Letra == letra:
                contadorLetras += 1
                cont +=1
        return contadorLetras

def InvertirPalabra(invertirPalabra):

    if invertirPalabra == 0 :
        return 1

def potencia(base ,exponente):
    if exponente==0:
        return 1
    else:
        return base* exponente(base ,exponente-1)

#/base = int(input("ingrese la base"))
#/exponente = int(input("ingrese la exponente"))
#/print(potencia(base,exponente))


while True:
    menu()
    op = int(input("\nIngrese la opcion: "))

    match op:
        case 1:
            n= int(input("Ingrese un entero positivo: "))
            print(factorial(n))

        case 2:
            numNatural= int(input("Ingrese un entero positivo: "))
            print(NumeroNatural(numNatural))



