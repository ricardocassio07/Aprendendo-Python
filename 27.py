# 27. Crie um programa que verifique se uma pessoa é maior de idade.
idade = (int(input("Digite a sua idade em anos: ")))
if (idade >= 18):
    resultado = "maior de idade"
else:
    resultado = "menor de idade"
print("Você tem {} anos, portanto, você é {}".format(idade, resultado))