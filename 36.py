# 36. Escreva um programa que verifique se uma senha é válida.
print("A senha deve conter apenas NÚMEROS INTEIROS e 6 DIGÍTOS!!!")
try:
    s = (int(input("Digite a senha: ")))
    s = str(s)
    if (len(s) == 6):
        print("A senha digitada é VÁLIDA!!!")
    else:
        print("A senha digitada é INVÁLIDA!!!")
except ValueError:
    print("VOCÊ DEVE INSERIR APENAS NÚMERO INTEIROS!!!")