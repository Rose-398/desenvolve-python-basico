n=int(input("Digite a quantidade de experimentos registrados: "))
cont=0
cobaia_sapo, cobaia_rato, cobaia_coelho = 0, 0, 0

while cont<n:
    qtde_cobaia=int(input("Digite a quantidade de cobaias:"))
    tipo_cobaia=input("Digite o tipo da cobaia (S:Sapo, R:Rato ou C:Coelho)")
    if tipo_cobaia=="S":
        cobaia_sapo=cobaia_sapo+qtde_cobaia
    elif tipo_cobaia=="R":
        cobaia_rato=cobaia_rato+qtde_cobaia
    elif tipo_cobaia=="C":
        cobaia_coelho=cobaia_coelho+qtde_cobaia
    else:
        print("Tipo de cobaia inválido!")
    cont=cont+1
total_cobaias=cobaia_sapo+cobaia_coelho+cobaia_rato
sapo_percent=cobaia_sapo/total_cobaias*100
rato_percent=cobaia_rato/total_cobaias*100
coelho_percent=cobaia_coelho/total_cobaias*100
print(f"Total: {total_cobaias:.0f}")
print(f"Total de coelhos: {cobaia_coelho}")
print(f"Total de ratos: {cobaia_rato}")
print(f"Total de sapos: {cobaia_sapo}")
print(f"Percentual de coelhos: {coelho_percent}%")
print(f"Percentual de ratos: {rato_percent}%")
print(f"Percentual de sapos: {sapo_percent}%")