#Moisés Gutiérrez Guerrero
#10/10/24
#Mejora el programa NUMEROS_PARES para que la pregunta se repita si el usuario no contesta S,s,N o n.


cont = 0
seguir = "s"

while seguir == "S" or seguir == "s":
    par = int(input("Escriba un numero par: "))
    
    if par % 2 == 0:
        cont = cont + 1
    else:
        while par % 2 != 0:
            par = int(input(str(par)+" no es un numero par. Inténtelo de nuevo: "))
        cont = cont + 1
    seguir = input("¿Quiere escribir otro número par? (S/N): ")

#mejora ------------
    while seguir not in ["S", "s", "N", "n"]:
        seguir = input("¿Quiere escribir otro número par? (S/N): ")
    
print("Ha escrito",cont,"numeros pares.")