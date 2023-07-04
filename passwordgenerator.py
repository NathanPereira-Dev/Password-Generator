import random
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']#52
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']#10
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']#9

print("Bem vindo ao Gerador de Senha!")
nr_letras= int(input("Quantas letras você gostaria de ter em sua senha?\n")) 
nr_simbolos = int(input(f"Quantos simbolos gostaria?\n"))
nr_numeros = int(input(f"Quantos números gostaria?\n"))

lista_senha = []
for char in range(1, nr_letras +1):
    lista_senha.append(random.choice(letras))
for char in range(1, nr_simbolos +1):
    lista_senha.append(random.choice(simbolos))
for char in range(1, + nr_numeros +1):
    lista_senha.append(random.choice(numeros))

senha = ""
for char in lista_senha:
    senha += char
print(f"A sua senha é: {senha}")