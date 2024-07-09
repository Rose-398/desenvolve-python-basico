#2) Leia um valor inteiro correspondente a uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius. Fórmula de conversão: C = (F - 32) * (5/9), sendo C o valor em graus Celsius e F o valor em Fahrenheit. Antes de imprimir, converta o valor em Celsius para inteiro. A mensagem deve estar formatada da seguinte maneira: 86 graus Fahrenheit são 30 graus Celsius.#

print("Conversão de temperatura: Celsius para Fahreheit")
graus_f=int(input("Digite a temperatura em Fahrenheit:"))
graus_c= int((graus_f - 32) * (5/9))
print(f"{graus_f} graus Fahrenheit são {graus_c} graus Celsius.")