

cont=0
suma=0
seguir= True

while seguir:
    n = input("Introduce un numero: \n")
    if n =="":
        seguir = False
    else:
        cont = cont+1
        suma = suma + eval(n)

print("N datos:", cont)
print("Suma:", suma)