# 12. Crie um program que troque o valor de duas variáveis.
x = (float(input("Digite um valor para x: ")))
y = (float(input("Digite um valor para y: ")))
temporario = x
x = y
y = temporario
print("x = {}\ny = {}".format(x, y))