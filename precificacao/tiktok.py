tiktok_comissao = 0.12
taxa_fixa = 4

def calculo_shopee(vproduto, lucro):
    pvenda = (vproduto + lucro + taxa_fixa) / (1 - tiktok_comissao)
    taxa = (pvenda * tiktok_comissao) + taxa_fixa
    return {
        "pvenda": pvenda,
        "taxa": taxa
    }