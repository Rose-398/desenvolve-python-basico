#4) Você está implementando um sistema de entrega expressa e precisa calcular o valor do frete com base na distância e no peso do pacote. Escreva um código que solicita a distância da entrega em quilômetros e o peso do pacote em quilogramas. O programa deve calcular e imprimir o valor do frete de acordo com as seguintes regras:
#Distância até 100 km: R$1 por kg.
#Distância entre 101 e 300 km: R$1.50 por kg.
#Distância acima de 300 km: R$2 por kg.
#Acrescente uma taxa de R$10 para pacotes com peso superior a 10 kg


distancia=float(input("Informe a distância em km: "))
peso=float(input("informe o peso da mercadoria em kg: "))
taxa=10

if peso>10:
    taxa=10
    if distancia<=100:
        frete=peso*1+taxa
    else:
        if distancia>=101 and distancia<=300:
            frete=peso*1.5+taxa
        else:
            frete=peso*2+taxa
else:
    if distancia<=100:
        frete=peso*1
    else:
        if distancia>=101 and distancia<=300:
            frete=peso*1.5
        else:
            frete=peso*2
print(f"O valor do frete é: {frete}.")