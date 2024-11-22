

lista1 = ["pepe","jose","a",1234,"arroz"]
lista2 = list(range(2,20,4))
lista3 = []
for i in lista1:
    lista3.append(i)
for i in lista2:
    lista3.append(i)

print("la union de la lista",lista1, "y la lista", lista2,"es", lista3)