#Moisés Gutiérrez Guerrero
#03/10/2024
#Programa que pide una cantidad de segundos y devuelve cuantos minutos y segundos son.

segundos=input("Escriba una cantidad de segundos: ")

min = eval(segundos) // 60
seg = eval(segundos) % 60

print(segundos,"segundos son",min,"minutos y",seg,"segundos")