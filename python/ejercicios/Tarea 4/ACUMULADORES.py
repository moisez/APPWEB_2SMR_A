#Moisés Gutiérrez Guerrero
#10/10/24
#Escriba un programa que pida dos números enteros positivos y te diga la suma desde el primer número hasta el segundo


n1 = int(input("Escriba un numero entero: "))

if n1 < 0:
    print("Le he pedido un numero entero positivo")
    
else:
    n2 = int(input("escriba un numero entero mayor que " + str(n1) + ": "))
    if n2 <= n1:
        print("Le he pedido un numero mayor que ", n1)
    else:
        y = 0
        for x in range(n1,n2+1):
            y = y + x
            
print("La suma desde",n1 ,"hasta",n2 ,"es",y)