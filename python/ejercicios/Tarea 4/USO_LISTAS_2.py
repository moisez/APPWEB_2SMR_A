#Moisés Gutiérrez Guerrero
#06/10/24
#Escriba un programa que pida dos números enteros y escriba la lista de números consecutivos que hay entre ellos, de menor a mayor.

x = int(input("introduce un número entero: "))
y = int(input("introduce otro número entero: "))

if x<y:
    print(list(range(x+1,y)))
else:
    print(list(range(y+1,x)))