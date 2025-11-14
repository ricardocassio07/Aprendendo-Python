# 40. Escreva um programa que classifique a temperatura.
t = (float(input("Digite a temperatura em °C: ")))
if (t >= 35):
    print("{}°C: HUUUU!!! Que calor é esse!? Só queria uma piscininha agora!!! 😎😎😎".format(t))
elif (t >= 26):
    print("{}°C: Está enquentando, hein! Só queria uma limonada e uma prainha agora!!! 🍋🍹🏖️".format(t))
elif (t >= 16):
    print("{}°C: Que clima bom! Agora é separar o protetor solar e ir dar uma volta no parque!!! 🏕️🏕️🏕️".format(t))
elif (t >= 5):
    print("{}°C: Está frio, hein! Agora só uma coberta, um chocolate quente e um bom filme resolvem!!! 😁😁😁".format(t))
else:
    print("{}°C: ARGHHHH! Está extremamente frio!!! 🥶🥶🥶".format(t))