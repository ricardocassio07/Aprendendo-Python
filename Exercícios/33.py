# 33. Crie um programa que verifique se um número está em um intervalo.
inicio_intervalo = (int(input("Digite o número INTEIRO que você deseja que seja o INÍCIO do intervalo: ")))
fim_intervalo = (int(input("Digite o número INTEIRO que você deseja que seja o FIM do intervalo: ")))
n = (int(input("Digite um número INTEIRO qualquer: ")))
if (inicio_intervalo > fim_intervalo):
    temporario = inicio_intervalo
    inicio_intervalo = fim_intervalo
    fim_intervalo = temporario
if (inicio_intervalo < n < fim_intervalo):
    print("O número {} está entre {} e {}".format(n, inicio_intervalo, fim_intervalo))
else:
    print("O número {} não está entre {} e {}".format(n, inicio_intervalo, fim_intervalo))