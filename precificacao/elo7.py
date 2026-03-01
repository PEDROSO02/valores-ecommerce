elo7_comissao = 0.12
taxa_fixa_elo7 = 3.00

def calculo_elo(vproduto, lucro):

    pvenda = (vproduto + taxa_fixa_elo7 + lucro) / (1 - elo7_comissao)
    taxa = (pvenda * elo7_comissao) + taxa_fixa_elo7

    return {
        "pvenda": round(pvenda, 2),
        "taxa": round(taxa, 2),
        "lucro": round(lucro, 2)
    }