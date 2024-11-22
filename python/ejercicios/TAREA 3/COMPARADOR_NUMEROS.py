#Moisés Gutiérrez Guerrero
#04/10/24
#Escriba un programa que pida tres números y que escriba si son los tres iguales, si hay dos iguales o si son los tres distintos.

n1 = input("Escribe un numero: ")
n2 = input("Escribe otro numero: ")
n3 = input("Escribe un numero más: ")

if  n1==n2 and n2==n3:
    print("Ha escrito tres veces el mismo número.")
elif n1==n2 or n2==n3 or n1==n3:
    print("Ha escrito uno de los numeros dos veces.")
else:
    print("Los tres números que ha escrito son distintos.")
