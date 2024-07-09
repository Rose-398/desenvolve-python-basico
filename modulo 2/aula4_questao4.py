#4) Escreva um programa que leia um valor inteiro referente a uma quantia em reais e calcule a menor quantidade possível de notas necessárias para pagar aquele valor. As notas possíveis são: 100, 50, 20, 10, 5, 2, 1. A saída deve estar formatada exatamente como indicado. 
titulo=("Cálculo da quantidade minima de notas para pagar determinado valor.")
print('\033[1m' + titulo + '\033[0m')
#ENTRADA DE DADOS
valor_brl=int(input("\033[3mDigite o valor em reais: \033[0m"))
#CALCULO DO VALOR
nota_100=valor_brl//100
saldo_brl=valor_brl-nota_100*100
nota_50=saldo_brl//50
saldo_brl=saldo_brl-nota_50*50
nota_20=saldo_brl//20
saldo_brl=saldo_brl-nota_20*20
nota_10=saldo_brl//10
saldo_brl=saldo_brl-nota_10*10
nota_5=saldo_brl//5
saldo_brl=saldo_brl-nota_5*5
nota_2=saldo_brl//2
saldo_brl=saldo_brl-nota_2*2
nota_1=saldo_brl//1
saldo_brl=saldo_brl-nota_1*1

#SAÍDA DE DADOS COM FORMATAÇÃO
print(f"{nota_100} notas de R$100,00")
print(f"{nota_50} notas de R$50,00")
print(f"{nota_20} notas de R$20,00")
print(f"{nota_10} notas de R$10,00")
print(f"{nota_5} notas de R$5,00")
print(f"{nota_2} notas de R$2,00")
print(f"{nota_1} notas de R$1,00")