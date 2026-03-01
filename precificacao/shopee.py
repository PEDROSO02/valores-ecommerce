shopee_comissao = 0.2
taxa_fixa = 4

def calculo_shopee(vproduto, lucro):
    pvenda = (vproduto + lucro + taxa_fixa) / (1 - shopee_comissao)
    taxa = (pvenda * shopee_comissao) + taxa_fixa
    return {
        "pvenda": pvenda,
        "taxa": taxa
    }