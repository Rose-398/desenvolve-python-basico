#1) Faça um programa para ler as dimensões de um terreno em inteiros (comprimento e largura), bem como o preço do metro quadrado da região em ponto flutuante. Calcule o valor do terreno e imprima o resultado com a formatação apresentada a seguir. O terreno possui 250m2 e custa R$512,490.50.Comente na linha acima de cada instrução uma breve descrição da instrução. Fórmulas:  area_m2 = comprimento * largura   preco_total = preco_m2 * area_m2#

print("Cálculo do valor de um terreno")
comprimento=int(input("Digite o comprimento do terreno:")) #entrada de dados e definição do tipo "inteiro" para a variável comprimento
largura=int(input("Digite a largura do terreno:")) #entrada de dados e definição do tipo "inteiro" para a variável largura
preço_m2=float(input("Digite o preço do m2 do terreno:"))  #entrada de dados e definição do tipo "float" para a variável preço_m2
tamanho_terreno=comprimento*largura  #calculo do tamanho do terreno 
valor_do_terreno=comprimento*largura*preço_m2  #calculo do valor do terreno
print(f"O terreno possui {tamanho_terreno} m2 e custa {valor_do_terreno:,.2f}")  #impressão na tela da frase que contem tamanho e valor do terreno,com formatação


