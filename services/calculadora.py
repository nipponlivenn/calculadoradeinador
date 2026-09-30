def menu ():
    
    print('calculadoradeinador')
    print('suma')
    print('resta')
    print('multiplicacion')
    print('division')
    print('salir')
    
def numeros ():
    while True :
        try:
            numero1 = float(input('ingresa numero uno:'))
            numero2 = float(input('ingresa numero dos:'))
            return numero1, numero2
        except ValueError:
            print('respuesta no valida, intente de nuevo')

def suma (numero1, numero2):
    resultado = numero1 + numero2
    return resultado

def resta (numero1, numero2):
    return numero1 - numero2

def multiplicacion (numero1, numero2):
    return numero1 * numero2

def division (numero1, numero2):
    if numero2 == 0 :
        return 'operacion no valida'
    resultado = numero1 / numero2
    return resultado
