# 37. Crie um programa que determine o desconto baseado no valor da compra.
v = (float(input("Digite o valor da compra: R$")))
if (v >= 5000):
    desc = ("25%")
    r = (v * 0.75)
elif (v >= 2500):
    desc = ("20%")
    r = (v * 0.80)
elif (v >= 1250):
    desc = ("15%")
    r = (v * 0.85)
elif (v >= 625):
    desc = ("10%")
    r = (v * 0.90)
elif (v >= 312.5):
    desc = ("5%")
    r = (v * 0.95)
if (v >= 312.5):
    print("O cliente recebeu {} de desconto na sua compra de R${:.2f} e agora ele pagará R${:.2f}!".format(desc, v, r))
else:
    print("O valor da compra do cliente de R${:.2f} não foi suficiente para ele se encaixar em alguma das condições de desconto!".format(v))