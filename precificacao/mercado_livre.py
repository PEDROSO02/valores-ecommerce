ml_comissao = 0.20
taxa_fixa_ml = 12.50

def calculo_ml(vproduto, lucro):

    pvenda = (vproduto + taxa_fixa_ml + lucro) / (1 - ml_comissao)
    taxa = (pvenda * ml_comissao) + taxa_fixa_ml

    return {
        "pvenda": round(pvenda, 2),
        "taxa": round(taxa, 2),
        "lucro": round(lucro, 2)
    }