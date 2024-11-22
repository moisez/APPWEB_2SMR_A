#Moisés Gutiérrez Guerrero
#10/10/24
#Escriba un programa que pregunte cuantos números se van a introducir, los pida y diga el mayor, el menor y la media aritmetica.

cantidad = eval(input("¿Cuantos valores va a introducir? "))
valores = []

if cantidad < 0:
    print("imposible")
else:
    for x in range(cantidad):
        n = float(input("escriba el número " + str(x+1) + ": "))
        valores.append(n)

    max = valores[0]
    min = valores[0]
    suma = 0

    for x in valores:
        suma = suma + x
        if x > max:
            max = x
        if x < min:
            min = x
        
    media = suma / cantidad

    print("El número más pequeño de los introducidos es ",min)
    print("El número más grande de los introducidos es ",max) 
    print("La media de los números introducidos es ",media)
