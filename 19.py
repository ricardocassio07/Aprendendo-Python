# 18. Crie um programa que calcule a velocidade média.
capital = (float(input("Digite o valor inicial da transação: R$")))
taxaDejuros = (float(input("Digite a taxa de juros:\nObs.: Digite apenas números não insira o sinal de %! Exemplo: Digite: '20' e não '20%'!\n-> ")))
taxaDejuros /= 100
print("Obs.: A taxa de juros e o tempo devem estar na mesma unidade. Se a taxa for anual, o tempo deve estar em anos; se for mensal, o tempo deve estar em meses.")
tempo = (float(input("Digite o tempo: ")))
jurosSimples = (capital * taxaDejuros * tempo)
print("Juros Simples = Capital x Taxa de Juros x Tempo = {:.2f} x {:.2f} x {:.1f} = R${:.2f}".format(capital, taxaDejuros, tempo, jurosSimples))