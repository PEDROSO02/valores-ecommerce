shopee = 0.2
ml = 0.2
taxa = 0
ts = 4
tml = 12.5

valor_produto = float(input("Digite o valor que você paga no produto: "))
print("Qual sua plataforma de venda?")

plataforma = int(input("Digite 1 para ML e 2 para Shopee"))
lucro = float(input("Qual lucro (em R$) deseja obter nesta venda? "))

if plataforma == 1:
    print("Realizando cálculo...")
    pv = (valor_produto + lucro + tml) / (1 - ml)
    taxa = (pv* ml) + tml
    print(f"A taxa cobrada pelo ML será de R$ {taxa:.2f}" )
    print(f"Para obter o lucro desejado, precisará vender o produto a R${pv:.2f}")
    
    
elif plataforma == 2:
     print("Realizando cálculo...")
     pv = (valor_produto + lucro + ts) / (1 - shopee)
     taxa = (pv * shopee) + ts
     print(f"A tala cobrada pela shopee será de R$ {taxa:.2f}" )
     print(f"Para obter o lucro desejado, precisará vender o produto a R${pv:.2f}")
     
else:
    print("A opção selecionada não é valida")
    


