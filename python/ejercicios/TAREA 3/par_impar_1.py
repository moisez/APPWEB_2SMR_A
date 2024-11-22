#Moisés Gutiérrez Guerrero
#02/10/24
#Introducir primero un numero par y luego un numero inpar. En caso de que uno de los dos valores no sea correcto, mostrar un unico aviso.

numpar = float(input("Introduce un numero par: "))
numimpar = float(input("Introduce un numero impar: "))

par = (numpar%2==0)
impar = (numimpar%2!=0)

if par and impar:
    print("maravilloso")
else: 
    print("No")