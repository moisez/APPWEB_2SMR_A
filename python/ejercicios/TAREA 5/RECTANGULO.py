#Moisés Gutiérrez Guerero
#12/10/2024
#Escribe un programa que pida la anchura y altura de un rectángulo y lo dibuje con caracteres producto.


def rectangulo(ancho,alto):
    for y in range(alto):
        print("* " * ancho)
        
ancho =int(input("Introduzca la anchura: "))
alto = int(input("Introduzca la altura: "))

rectangulo(ancho,alto)