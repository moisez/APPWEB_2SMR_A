#Moisés Gutiérrez Guerrero
#01/10/2024
#CALCULO DEL INDICE DE MASA CORPORAL INTRODUCIENDO EL PESO Y LA ALTURA

peso=float(input("¿Cuanto pesa?: "))
altura=float(input("Cuando mide en metros?: "))
imc = (peso / (altura**2))

print("Su imc es ", round(imc,1))
print("Un imc my alto indica obesidad. Los valores normales de imc están entre 20 y 25, pero esos limites dependen de la edad, del sexo, de la constitución física, etc.")