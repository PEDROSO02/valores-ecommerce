ml_comissao = 0.2
taxa_fixa = 12.5

def calculo_ml(vproduto, lucro):
    pvenda = (vproduto + taxa_fixa + lucro) / (1 - ml_comissao)
    taxa = (pvenda * ml_comissao)+taxa_fixa
    return {
        "pvenda": pvenda,
        "taxa": taxa
    }