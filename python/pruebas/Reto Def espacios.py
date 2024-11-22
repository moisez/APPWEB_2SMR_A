#Escribe un programa que te diga cuantas palabras hay en una frase.
frase = "  Hola   amigo0    esta clase va a hacer       una huelga   a  "
cont = 0
palabra = False

for n in frase:
    if n != " ":
        if palabra == True :
            cont = cont +1
            palabra = False

    else:
        palabra = True



print(cont)
