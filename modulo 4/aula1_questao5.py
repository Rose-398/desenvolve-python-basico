n=int(input("Digite a quantidade de respondentes da pesquisa: "))
participante=0
soma_idade=0
cont=0
while cont<n:
    participante=participante+1
    idade=float(input(f"Digite a idade do participante {participante}: "))
    soma_idade=soma_idade+idade
    cont=cont+1
media_idade=soma_idade/n
print(f"A média das idades é: {media_idade:.0f} anos")
