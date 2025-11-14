# 60. Implemente um sistema de validação de CPF que verifique se o formato está correto, calcule os dígitos verificadores e trate todas as exceções possíveis.
try:
    CPF = (int(input("Digite o CPF (SEM TRAÇOS OU PONTOS): ")))
    CPF = str(CPF)
    if (len(CPF) == 11):
        n1 = CPF[0]
        n1 = int(n1)
        n2 = CPF[1]
        n2 = int(n2)
        n3 = CPF[2]
        n3 = int(n3)
        n4 = CPF[3]
        n4 = int(n4)
        n5 = CPF[4]
        n5 = int(n5)
        n6 = CPF[5]
        n6 = int(n6)
        n7 = CPF[6]
        n7 = int(n7)
        n8 = CPF[7]
        n8 = int(n8)
        n9 = CPF[8]
        n9 = int(n9)
        n10 = CPF[9]
        n10 = int(n10)
        n11 = CPF[10]
        n11 = int(n11)
        if (n1 == n2 == n3 == n4 == n5 == n6 == n7 == n8 == n9 == n10 == n11):
            print("CPF INVÁLIDO!!! ELE NÃO PODE SER UMA SEQUÊNCIA JÁ CONHECIDA!!!")
        else:
            digito10 = ((n1 * 10) + (n2 * 9) + (n3 * 8) + (n4 * 7) + (n5 * 6) + (n6 * 5) + (n7 * 4) + (n8 * 3) + (n9 * 2))
            r = (digito10 % 11)
            if (r < 2):
                digito10 = 0
            else:
                digito10 = (11 - r)
            digito11 = ((n1 * 11) + (n2 * 10) + (n3 * 9) + (n4 * 8) + (n5 * 7) + (n6 * 6) + (n7 * 5) + (n8 * 4) + (n9 * 3) + (n10 * 2))
            r = (digito11 % 11)
            if (r < 2):
                digito11 = 0
            else:
                digito11 = (11 - r)

            if ((n10 != digito10) or (n11 != digito11)):
                print("CPF INVÁLIDO!!!")
            else:
                print("O CPF {}{}{}.{}{}{}.{}{}{}-{}{} É VÁLIDO!!!".format(n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11))
    else:
        print("O CPF É INVÁLIDO, POIS ELE DEVE CONTER EXATAMENTE 11 DIGITOS!!!")
except ValueError:
    print("DIGITE APENAS NÚMEROS!!!")