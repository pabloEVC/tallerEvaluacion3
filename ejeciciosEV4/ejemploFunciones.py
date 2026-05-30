#funciones
def sumanumeros():
    """Función que suma dos números ingresados por el usuario."""
    num1=int(input("ingrese numero 1: "))
    num2=int(input("ingrese numero 2: "))

    suma=num1+num2
    return suma

print(sumanumeros())