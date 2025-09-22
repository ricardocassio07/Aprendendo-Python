# 52. Desenvolva um sistema de notas que calcule média, identifique aprovação/reprovação e trate entradas inválidas.
valido = False
while (valido == False):
    try:
        n1 = (float(input("Digite a primeira nota: ")))
        n2 = (float(input("Digite a segunda nota: ")))
        n3 = (float(input("Digite a terceira nota: ")))
        n4 = (float(input("Digite a terceira nota: ")))
        if ((0 <= n1 <= 10) and (0 <= n2 <= 10) and (0 <= n3 <= 10) and (0 <= n4 <= 10)):
            media = ((n1 + n2 + n3 + n4) / 4)
            if (media >= 6):
                situacao = ("está APROVADO!")
            elif (media == 5):
                situacao = ("fará EXAME!")
            else:
                situacao = ("está REPROVADO!")
            print("A média entre as notas {}, {}, {} e {} é igual a {} e o aluno {}".format(n1, n2, n3, n4, media, situacao))
            valido = True
        else:
            print("TODAS AS NOTAS DEVEM SER MAIOR OU IGUAL A 0 E MENOR OU IGUAL A 10!")
    except ValueError:
        print("VOCÊ DEVE DIGITAR APENAS NÚMEROS!!!")