elo_comissao = 0.2
taxa_fixa = 4

def calculo_elo(vproduto, lucro):
    pvenda = (vproduto + lucro + taxa_fixa) / (1 - elo_comissao)
    taxa = (pvenda * elo_comissao) + taxa_fixa
    return {
        "pvenda": pvenda,
        "taxa": taxa
    } 