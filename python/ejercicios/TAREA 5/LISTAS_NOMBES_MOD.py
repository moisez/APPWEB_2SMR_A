#Moisés Gutiérrez Guerero
#12/10/2024
#Escriba una funcion que pida cuantas listas se quieren crear y solicite a continuación las palabras para cada lista y al final se muestren.


#Definimos la función
def crear_listas():
    
#Solicita la cantidad de listas
    cantidad = int(input("¿Cuántas listas quiere escribir? "))
    listas=[]
    
#Solicita las palabras para cada lista y las almacena primero en una lista y a continuación almacena la lista en otro lista.
    for x in range (cantidad):
        lista = []
        num_palabras = int(input("Digame cuantas palabras tiene la lista " + str(x+1)+": "))
        for i in range(num_palabras):
            palabra = input("digame la palabra "+str(i+1)+": ")
            lista.append(palabra)
        listas.append(lista)
        
#Muestra las listas
    for indice in range(len(listas)):
        print("La lista",indice+1,"es:",listas[indice])
        
#llamamos a la función
crear_listas