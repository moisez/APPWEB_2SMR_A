#Moisés Gutiérrez Guerrero
#02/10/24
#Programa que pide dos numeros enteros y calcula su división, escribiendo si la división es exacta o no.

Dividendo = int(input("Escriba el dividendo: "))
Divisor = int(input("Escriba el divisor: "))
Division = int(Dividendo/Divisor)
Exacto =(Dividendo%Divisor==0)
if Exacto:
    print("La división es exacta. Cociente:", Division) 
else:
    print("La division no es exacta. Cociente: Resto:", Dividendo%Divisor)