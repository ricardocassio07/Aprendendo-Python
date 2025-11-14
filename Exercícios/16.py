# 16. Crie um progrma que converta segundos em hors, minutos e segundos.
tempo_em_segundos = (float(input("Digite um tempo em segundos: ")))
tempo_em_minutos = (tempo_em_segundos / 60)
tempo_em_horas = (tempo_em_segundos / 3600)
tempo_em_segundos = tempo_em_segundos
print("{} segundos = {} horas = {} minutos = {} segundos".format(tempo_em_segundos, tempo_em_horas, tempo_em_minutos, tempo_em_segundos))