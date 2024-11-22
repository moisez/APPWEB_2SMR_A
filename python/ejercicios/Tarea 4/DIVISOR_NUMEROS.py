#Moisés Gutiérrez Guerrero
#06/10/24
#Escriba un programa que pida un número entero mayor que cero y escriba sus divisores.


n = int(input("Escriba un número entero mayor que cero: "))

if n <= 0:
    print("¡Caballera, le he pedido un numero entero mayor que cero!")
else:
    lista = []
    for x in range(1,n+1):
        if n % x == 0:
            lista.append(x)
    print("Los divisores de",n,"son:", lista)
        