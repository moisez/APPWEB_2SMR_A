#Moisés Gutiérrez Guerrero
#10/10/24
#Escriba un programa que pida la cantidad de números positivos que se tienen que escribir y a continuación pida números hasta que se haya escrito la cantidad de números positivos indicada.

cantidad = eval(input("Escriba la cantidad de números positivos a escribir: "))
cont=0
positivo=0

while cantidad <= 0:
    cantidad = eval(input("La cantidad debe ser mayor que 0. Inténtelo de nuevo: "))
    
for x in range(cantidad):
    if x == 0:
        n = eval(input("Escriba un numero: "))
        cont = cont + 1
        if n >= 0:
            positivo = positivo + 1           
    if positivo < cantidad:
        while positivo < cantidad:
            n = eval(input("Escriba otro número: "))
            cont = cont + 1
            if n >= 0:
                positivo = positivo + 1
            
print("Ha escrito",cont,"numeros,",positivo,"de ellos positivos")