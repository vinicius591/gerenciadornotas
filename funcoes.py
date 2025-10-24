def calcular_media(numero):
    if len(numero) == 0:
        return 0
    media = sum(numero) / len(numero)
    return media
valores = input("Digite suas notas")
valores = [float(n) for n in valores.split ()]