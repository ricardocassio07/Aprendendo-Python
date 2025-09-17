# 31. Crie um programa que verifique se um ano é bissexto.
a = (int(input("Digite um ano: ")))
if (a % 4 == 0 and (a % 100 != 0 or a % 400 == 0)):
    print("O ano de {} é bissexto!".format(a))
else:
    print("O ano de {} não é bissexto!".format(a))