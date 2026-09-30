from services.calculadora import menu, numeros, suma, resta, multiplicacion, division

while True:
    menu()
    opcion = int(input('elige una opcion:'))
    if opcion == 1 :
        numero1, numero2 = numeros ()
        print('el resultado es: ', suma (numero1, numero2))
    
    elif opcion == 2 :
        numero1, numero2 = numeros ()
        print('el resultado es: ' , resta (numero1, numero2))
        
    elif opcion == 3 :
        numero1, numero2 = numeros ()
        print('el resultado es: ' , multiplicacion (numero1, numero2))

    elif opcion == 4 :
        numero1, numero2 = numeros ()
        print('el resultado es: ' , division (numero1, numero2))

    elif opcion == 5 :
        print('gracias por usar el caladoradeinador, sus cuentas bancarias estan siendo vaciadas en este momento')
        break

    else:
        print('operacion no valida')
