n=float(input("Digite o valor de n: "))
maior=0

while n>0:
    x=float(input("Digite o valor de x: "))
    while x>maior:
        maior=x
    n=n-1
print(maior)
