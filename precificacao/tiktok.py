tiktok_comissao = 0.16
taxa_fixa_tiktok = 4.00

def calculo_tiktok(vproduto, lucro):

    pvenda = (vproduto + taxa_fixa_tiktok + lucro) / (1 - tiktok_comissao)
    taxa = (pvenda * tiktok_comissao) + taxa_fixa_tiktok

    return {
        "pvenda": round(pvenda, 2),
        "taxa": round(taxa, 2),
        "lucro": round(lucro, 2)
    }