n1=float(input("Digite o valor da nota 1: "))
n2=float(input("Digite o valor da nota 2: "))
n3=float(input("Digite o valor da nota 3: "))
m=(n1+n2+n3)/3

if m>=60:
    print('"Aprovado"')
elif m>=40:
    print('"Recuperaçao"')
else:
    print('"Reprovado"')
print('"Fim"')