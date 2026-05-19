menu=0
total=0
pikachu=0
otaku=0
pulpo=0
anguila=0
contador=0
subtotal=0
descuento=0
while True:
    while menu!=5:
        while True:
            try:
                
                print("menu de sushis:")
                print("1. Pikachu Roll $4500")
                print("2. Otaku Roll $5000")
                print("3. Pulpo Roll $5200")
                print("4. Anguila Roll $4800")
                print("5. Salir")
                menu=int(input("Bienvenido al restaurante de sushi, por favor elija su orden: "))
                if menu<1 or menu>5:
                    
        
                    print("Opción no válida, por favor elija una opción del 1 al 5.")
                else:
                    break
            except ValueError:
                print("Entrada no válida, por favor ingrese un número del 1 al 5.")
            
        if menu==1:
            print("usted ha elegido el Pikachu Roll")
            total+=4500
            pikachu+=1
            contador+=1
        elif menu==2:
            print("usted ha elegido el Otaku Roll")
            total+=5000
            otaku+=1
            contador+=1
        elif menu==3:
            print("usted ha elegido el Pulpo Roll")
            total+=5200
            pulpo+=1
            contador+=1
        elif menu==4:
            print("usted ha elegido el Anguila Roll")
            total+=4800
            anguila+=1
            contador+=1
        elif menu==5:
            break
    if menu==5:
        break
while True:

    codigo=input("ingrese el codigo de descuento si no posse uno solo ingrese x:").lower()
    
    if codigo=="soyotaku":
        
        print("¡Felicidades! Ha obtenido un descuento del 10%.")
        descuento=total*0.10
        subtotal=total-descuento
        break
    elif codigo=="x":
        print("No se ha aplicado ningún descuento.")
        subtotal=total
        break
    else:
        print("Código de descuento no válido, por favor intente nuevamente.")
print("*********************************")
print(f"total de productos: {contador}")
print("*********************************")
print("Usted ha comprado", pikachu, "Pikachu Rolls")
print("Usted ha comprado", otaku, "Otaku Rolls")
print("Usted ha comprado", pulpo, "Pulpo Rolls")
print("Usted ha comprado", anguila, "Anguila Rolls")
print(f"Total a pagar: ${total}")
print(f"Descuento aplicado: ${descuento}")
print(f"Subtotal a pagar: ${subtotal}")