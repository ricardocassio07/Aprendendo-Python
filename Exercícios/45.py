# 45. Crie um programa que verifique se uma data é válida (formato simples).
dia = (int(input("Comece digitando o dia: ")))
mes = (int(input("Agora digite o mês: ")))
ano = (int(input("Por fim, digite o ano: ")))
valido = ("sim")
if ((dia <= 30) and (mes == 4 or mes == 6 or mes == 9 or mes == 11)):
    valido = ("sim")
elif (dia <= 31) and (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
    valido = ("sim")
elif ((dia <= 29) and (mes == 2)and (ano % 4 == 0)):
    valido = ("sim")
elif ((dia <= 28) and (mes == 2) and (ano % 4 != 0)):
    valido = ("sim")
else:
    valido = ("não")
if (valido == ("sim")):
    print("A data {}/{}/{} É VÁLIDA!!!".format(dia, mes, ano))
else:
    print("A data {}/{}/{} NÃO É VÁLIDA!!!".format(dia, mes, ano))
    