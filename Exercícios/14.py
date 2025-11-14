# 14. Crie um programa que calcule o desconto de um produto.
valor = (float(input("Digite o valor do produto:\n-> R$")))
desconto = (float(input("Digite a porcentagem de desconto:\nObs.: Digite apenas números não insira o sinal de %! Exemplo: Digite: '20' e não '20%'!\n-> ")))
resultado = (valor - ((desconto / 100) * valor))
print("O valor inicial do produto de R${:.2f} com aplicação de um desconto de {:.2f}%, faz com que ele passe a custar R${:.2f}!".format(valor, desconto, resultado))