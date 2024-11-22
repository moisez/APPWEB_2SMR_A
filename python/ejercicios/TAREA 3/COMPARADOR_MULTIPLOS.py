#Moisés Gutiérrez Guerrero
#04/10/24
#Escriba un programa que pida dos números enteros y que escriba si el mayor es múltiplo del menor. El programa debe avisar cuando se escriben valores negativos o nulos.

n1 = int(input("Escribe un número: "))
n2 = int(input("Escribe otro número: "))

if (n1==0 or n2==0) and (n1<0 or n2<0):
    print("Lo siento, este programa no admite valores nulos ni negativos")
elif n1==0 or n2==0:
    print("Lo siento, este programa no admite valores nulos")
elif n1<0 or n2<0:
    print("Lo siento, este programa no admite valores negativos")
elif n1>n2:
    if n1%n2==0:
        print(n1,"es multiplo de",n2)
    else:
        print(n1,"no es multiplo de",n2)
else:
    if n2%n1==0:
        print(n2,"es multiplo de",n1)
    else:
        print(n2,"no es multiplo de",n1)