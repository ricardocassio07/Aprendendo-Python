# 18. Crie um programa que calcule a velocidade média.
distancia = (float(input("Digite a distãncia do trajeto em metros: ")))
tempo = (float(input("Digite o tempo do trajeto em segundos: ")))
VM = (distancia / tempo)
print("Velocidade Média = {} metros / {} segundos = {} m/s".format(distancia, tempo, VM))