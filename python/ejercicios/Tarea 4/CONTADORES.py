#Moisés Gutiérrez Guerrero
#06/10/24
#Escriba un programa que pregunte cuantos números se van a introducir, pida esos números y escriba cuantos negativos ha introducido.


cantidad = int(input("¿cuántos números vas a introducir?: "))

cont = 0

while cantidad < 0:
    print("¡imposible!")
    cantidad = int(input("¿cuántos números vas a introducir?: "))
else: 
    for x in range(1,cantidad+1):
        n = int(input("introduce el número " + str(x) + ": "))
        if n < 0:
            cont = cont +1
    print("Has introducido", cont, "numeros negativos")