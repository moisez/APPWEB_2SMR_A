#Moisés Gutiérrez Guerrero
#04/10/24
#Escriba un programa que pida un año y que escriba si es bisiesto o no

a = int(input("Introduce un año: "))

if not a%4==0:
    print("Este año no es bisiesto")
elif a%4==0 and not a%100==0:
    print("El año",a,"es un año bisiesto porque es múltiplo de 4 sin ser múltiplo de 100")
elif a%400==0:
    print("El año",a,"es un año bisiesto porque es multiplo de 400")
else: 
    a%100 and not a%400==0
    print("El año",a,"no es un año bisiesto porque es múltiplo de 100 sin ser múltiplo de 400")
    
        