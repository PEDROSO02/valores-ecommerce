shopee_comissao = 0.20
taxa_fixa_shopee = 4.00

def calculo_shopee(vproduto, lucro):

    pvenda = (vproduto + taxa_fixa_shopee + lucro) / (1 - shopee_comissao)
    taxa = (pvenda * shopee_comissao) + taxa_fixa_shopee

    return {
        "pvenda": round(pvenda, 2),
        "taxa": round(taxa, 2),
        "lucro": round(lucro, 2)
    }