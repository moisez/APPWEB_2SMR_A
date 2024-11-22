#Moisés Gutiérrez Guerero
#12/10/2024
#Escriba un programa que dibuje un triangulo


def triangulo(ancho):
    for x in range(ancho):
        print("* " * x)
    for x in range(ancho,0,-1):
        print("* " * x)
    print()
        
ancho = int(input("introduce el ancho del triangulo: "))

triangulo(ancho)