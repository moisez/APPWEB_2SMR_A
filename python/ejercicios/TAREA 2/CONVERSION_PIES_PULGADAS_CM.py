#Moisés Gutiérrez Guerrero
#02/10/2024
#CONVERSOR DE PIES Y PULGADAS A CENTIMETROS

pies=input("Escriba una cantidad de pies: ")
pulgadas=input("Escriba una cantidad de pulgadas: ")
n1 = float(pies)* (12*2.54)
n2 = float(pulgadas)* 2.54
print(pies,"pies y",pulgadas,"pulgadas son",n1+n2, "cm")