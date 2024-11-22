#Moisés Gutiérrez Guerrero
#10/10/24
#Escriba un programa que pida números pares mientras el usuario indique que quiere seguir introduciendo números.
#Para indicar que quiere seguir escribiendo números, el usuario deberá contestar S o s a la pregunta.


cont = 0
seguir = "s"

while seguir == "S" or seguir == "s":
    par = int(input("Escriba un numero par: "))
    
    if par % 2 == 0:
        cont = cont + 1
    else:
        while par % 2 != 0:
            par = int(input(str(par)+"no es un numero par. Inténtelo de nuevo: "))
        cont = cont + 1
    seguir = input("¿Quiere escribir otro número par? (S/N): ")
    
print("Ha escrito",cont,"numeros pares.")

