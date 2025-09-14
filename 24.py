# 24. Crie um programa que calcule o resto da divisão.
dividendo = (float(input("Digite um número que você deseja que seja dividido: ")))
divisor = (float(input(f"Digite um número que irá dividir o número {dividendo}: ")))
resultado = (dividendo % divisor)
print("O resto da divisão entre {} e {} é igual a {}".format(dividendo, divisor, resultado))