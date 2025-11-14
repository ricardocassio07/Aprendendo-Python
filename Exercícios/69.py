# 69. Crie um sistema de cronômetro que use range para contar regressivamente.
# Importando a biblioteca 'time':
import time
# Entradas de dados:
while True:
    try:
        qtdeHoras = (int(input("Digite a quantidade de horas que deseja cronometrar: ")))
        while (qtdeHoras < 0):
            print("QUANTIDADE DE HORAS INVÁLIDA!!!")
            qtdeHoras = (int(input("Digite a quantidade de horas que deseja cronometrar: ")))
        break
    except:
        print("DIGITE APENAS NÚMEROS!!!")

while True:
    try:
        qtdeMinutos = (int(input("Digite a quantidade de minutos que deseja cronometrar: ")))
        while ((0 < qtdeMinutos) and (qtdeMinutos > 59)):
            print("QUANTIDADE DE MINUTOS INVÁLIDA!!!")
            qtdeMinutos = (int(input("Digite a quantidade de minutos que deseja cronometrar: ")))
        break
    except:
        print("DIGITE APENAS NÚMEROS!!!")
     
while True:
    try:
        qtdeSegundos = (int(input("Digite a quantidade de segundos que deseja cronometrar: ")))
        while ((0 < qtdeSegundos) and (qtdeSegundos > 59)):
            print("QUANTIDADE DE SEGUNDOS INVÁLIDA!!!")
            qtdeSegundos = (int(input("Digite a quantidade de segundos que deseja cronometrar: ")))
        break
    except:
        print("DIGITE APENAS NÚMEROS!!!")

# tempoTotal em execuções do range:
tempoTotal = ((qtdeHoras * 3600) + (qtdeMinutos * 60) + (qtdeSegundos))
segundos = 0
minutos = 0
horas = 0

# Crônometro:
for i in range(1, (tempoTotal + 1)):
    # Esperar 1 segundo para mostrar o próximo valor:
    time.sleep(1)
    # Adicionar nos contadores
    segundos += 1
    if ((i > 0) and ((i % 60) == 0)):
        segundos = 0
        minutos += 1
    if (minutos == 60):
        minutos = 0
        horas += 1
    # Formatação: HH:MM:SS
    S = str(segundos)
    M = str(minutos)
    H = str(horas)
    if (len(S) == 1):
        S = ("0" + S)
    if (len(M) == 1):
        M = ("0" + M)
    if (len(H) == 1):
        H = ("0" + H)
    # Mostrar:
    print("{0}:{1}:{2}".format(H, M, S))

