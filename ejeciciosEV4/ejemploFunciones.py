#funciones
import funciones
def funciones():
    """Función que solicita al usuario dos números y devuelve su suma."""
    num1=int(input("ingrese numero 1: "))


#funciones con parametros
def sumanumeros(num1,num2):
    """Función que suma dos números dados como parámetros."""
    suma=num1+num2
    return suma
numero1=int(input("ingrese numero 1: "))
numero2=int(input("ingrese numero 2: "))
print(sumanumeros(numero1,numero2))
