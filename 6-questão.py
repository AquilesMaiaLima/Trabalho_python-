nome = input("Escreva seu nome completo: ")
idade = int(input("sua idade: "))
if idade >= 16:
    i = "pode emitir o seu titulo de eleitor"
else:
    i = "não pode emitir o seu titulo de eleitor"
print(f"{nome} voce tem {idade} e {i}")