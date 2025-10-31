# 71. Crie um sistema de calendário que use range para gerar datas.
validoD1 = "não"
validoD2 = "não"
while ((validoD1 == "não") or (validoD2 == "não")):
    diaInicial = (int(input("Digite o dia da data inicial: ")))
    mesInicial = (int(input("Digite o mês da data inicial: ")))
    anoInicial = (int(input("Digite o ano da data inicial: ")))
    diaFinal = (int(input("Digite o dia da data final: ")))
    mesFinal = (int(input("Digite o mês da data final: ")))
    anoFinal = (int(input("Digite o ano da data final: ")))

    validoD1 = ("sim")
    if ((diaInicial <= 30) and (mesInicial == 4 or mesInicial == 6 or mesInicial == 9 or mesInicial == 11)):
        validoD1 = ("sim")
    elif (diaInicial <= 31) and (mesInicial == 1 or mesInicial == 3 or mesInicial == 5 or mesInicial == 7 or mesInicial == 8 or mesInicial == 10 or mesInicial == 12):
        validoD1 = ("sim")
    elif ((diaInicial <= 29) and (mesInicial == 2)and (anoInicial % 4 == 0)):
        validoD1 = ("sim")
    elif ((diaInicial <= 28) and (mesInicial == 2) and (anoInicial % 4 != 0)):
        validoD1 = ("sim")
    else:
        validoD1 = ("não")

    validoD2 = ("sim")
    if ((diaFinal <= 30) and (mesFinal == 4 or mesFinal == 6 or mesFinal == 9 or mesFinal == 11)):
        validoD2 = ("sim")
    elif (diaFinal <= 31) and (mesFinal == 1 or mesFinal == 3 or mesFinal == 5 or mesFinal == 7 or mesFinal == 8 or mesFinal == 10 or mesFinal == 12):
        validoD2 = ("sim")
    elif ((diaFinal <= 29) and (mesFinal == 2)and (anoFinal % 4 == 0)):
        validoD2 = ("sim")
    elif ((diaFinal <= 28) and (mesFinal == 2) and (anoFinal % 4 != 0)):
        validoD2 = ("sim")
    else:
        validoD2 = ("não")

    # Verificar se a data inicial não é maior que a final:
    somaDataInicial = (diaInicial + (mesInicial * 30) + (anoInicial * 365))
    somaDataFinal = (diaFinal + (mesFinal * 30) + (anoFinal * 365))
    if (somaDataInicial > somaDataFinal):
        validoD1 = ("não")

# Intervalo entre as datas:
while True:
    try:
        intervalo = (int(input("Qual o intervalo de dias que você deseja que tenha a cada data?\n-> ELE PODE SER DE 1 A 30 DIAS!!! <-\n-> ")))
        if (1 <= intervalo <= 365):
            print("Ok!")
            break
        else:
            print("O INTERVALO DEVE SER DE NO MINÍMO 1 DIA E NO MÁXIMO 365 (UM ANO)!!!")
    except:
        print("DIGITE APENAS NÚMEROS!!!")

# Quantidade de dias entre as duas datas:
qtdeDias = (somaDataFinal - somaDataInicial)

# Quantidade de vezes que será possível mostrar uma data, tendo em vista o intervalo de dias desejado pelo usuário:
qtdeVezes = (qtdeDias // intervalo)

dia = diaInicial
mes = mesInicial
ano = anoInicial

for i in range(qtdeVezes):
    dia += intervalo

    if dia > 30:
        addMeses = dia // 30
        dia = dia % 30
        if dia == 0:
            dia = 30
            addMeses -= 1

        mes += addMeses

        if mes > 12:
            addAnos = mes // 12
            mes = mes % 12
            if mes == 0:
                mes = 12
                addAnos -= 1
            ano += addAnos

    print("{0}/{1}/{2}".format(dia, mes, ano))
