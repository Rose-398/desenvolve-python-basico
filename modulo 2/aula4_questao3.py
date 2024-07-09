#Você está desenvolvendo um programa para calcular o preço total de uma compra em uma loja online. O preço dos produtos é calculado multiplicando a quantidade pelo preço unitário. Escreva um programa em Python que solicite do usuário o nome, o preço unitário e a quantidade de 3 produtos comprados e imprima ao final o preço total da compra. Note no exemplo a seguir que: Cada entrada de dados tem uma mensagem indicando o dado solicitado (mensagens em itálico, dado de entrada em negrito).A saída deve estar formatada exatamente como indicado (a string "Total: R$" e o preço com um separador de milhar e duas casas decimais).

#ENTRADA DE DADOS
p1=input("\033[3mDigite o nome do produto p1: \033[0am")
p_unit_1=float(input("\033[3mDigite o preço unitário do produto 1: \033[0m"))
q_p1=int(input("\033[3mDigite a quantidade do produto 1: \033[0m"))
p2=input("\033[3mDigite o nome do produto 2: \033[0m")
p_unit_2=float(input("\033[3mDigite o preço unitário do produto 2: \033[0m"))
q_p2=int(input("\033[3mDigite a quantidade do produto 2: \033[0m"))
p3=input("\033[3mDigite o nome do produto 3: \033[0m")
p_unit_3=float(input("\033[3mDigite o preço unitário do produto 3: \033[0m"))
q_p3=int(input("\033[3mDigite a quantidade do produto 3: \033[0m"))#CALCULO DO VALOR
valor_compra=p_unit_1*q_p1+p_unit_2*q_p2+p_unit_3*q_p3
#SAÍDA DE DADOS COM FORMATAÇÃO
print(f"Total: R${valor_compra:,.2f}.")
