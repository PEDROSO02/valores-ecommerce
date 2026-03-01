from precificacao import shopee, mercado_livre, elo7, tiktok

def main():
    valor = float(input("Custo total do produto: "))
    lucro = float(input("Lucro desejado: "))

    print("1 - Mercado Livre")
    print("2 - Shopee")
    print("3 - Elo 7")

    plataforma = int(input("Escolha: "))

    if plataforma == 1:
        resultado = mercado_livre.calculo_ml(valor, lucro)

    elif plataforma == 2:
        resultado = shopee.calculo_shopee(valor, lucro)
    
    elif plataforma == 3:
        resultado = elo7.calculo_elo(valor, lucro)

    else:
        print("Opção inválida!!!")
        return
    
    print(f"Taxa: R$ {resultado['taxa']: .2f}")
    print(f"Preço de venda: R$ {resultado['pvenda']: .2f}")

if __name__ == "__main__":
    main()