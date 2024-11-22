#Moisés Gutiérrez Guerrero
#02/10/24
#Introducir primero un numero par y si no es correcto mostrar un aviso, si es correcto pedirá introducir un numero impar y si el valor no es correcto mostrara un aviso.

numpar = float(input("Introduce un numero par: "))
par = (numpar %2 ==0)

if par:
    numimpar = float(input("introduce un numero impar: "))
    impar = (numimpar %2 !=0)
    if impar:
        print ("Gracias por su colaboración")
    else:
        print ("No se ha escrito un numero impar")
        print ("Ejecute de nuevo el programa para volver a intentarlo")
else:
    print ("No se ha escrito un numero par")
    print ("Ejecute de nuevo el programa para volver a intentarlo")