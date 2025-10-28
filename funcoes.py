
def calcular_media(listaNotas):
    media = sum(listaNotas) / len(listaNotas)
    return media

def situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media < 7 and media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"

