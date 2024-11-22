#Moisés Gutiérrez Guerrero
#03/10/2024
#Programa que pide una cantidad de segundos y devuelve cuantas horas, minutos y segundos son

segundos=int(input("Escriba una cantidad de segundo: "))

h = segundos // 3600
m = segundos % 3600 // 60
s = segundos % 60

print(segundos,"segundos son", h,"horas,",m,"minutos y",s,"segundos")