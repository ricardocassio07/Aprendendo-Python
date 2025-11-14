# 58. Desenvolva um sistema de cadastro de pessoas com validação de dados e busca.
pessoas = {
    "12345678909": {"nome": "Ana", "idade": 25, "cidade": "São Paulo"},
    "98765432100": {"nome": "Carlos", "idade": 30, "cidade": "Rio de Janeiro"},
    "45678912332": {"nome": "Mariana", "idade": 22, "cidade": "Belo Horizonte"},
    "32165498776": {"nome": "João", "idade": 28, "cidade": "Curitiba"}
}

encerrarSessao = False
while encerrarSessao == False:
    try:
        opcao = int(input("O que deseja fazer?\nDigite:\n1- Cadastrar pessoas;\n2- Listar pessoas;\n3- Buscar pessoas;\n4- Atualizar dados;\n5- Encerrar sessão.\n-> "))
        if (1 <= opcao <= 5):
            print("OPÇÃO VÁLIDA!!!")
            if (opcao == 1):
                nome = input("Digite o nome da pessoa que deseja cadastrar:\n-> ")
                while (nome.strip() == ""):
                    print("NOME INVÁLIDO!!!")
                    nome = input("Digite o nome da pessoa que deseja cadastrar:\n-> ")

                CPFValidado = False
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
                                CPFValidado = True
                    else:
                        print("O CPF É INVÁLIDO, POIS ELE DEVE CONTER EXATAMENTE 11 DIGITOS!!!")
                except ValueError:
                    print("DIGITE APENAS NÚMEROS!!!")

            
                valido = False
                while (valido == False):
                    try:
                        idade = (int(input("Digite a idade dessa pessoa:\n-> ")))
                        while (idade <= 0):
                            print("IDADE INVÁLIDA!!!")
                            idade = (int(input("Digite a idade dessa pessoa:\n-> ")))
                        valido = True
                    except ValueError:
                        print("DIGITE APENAS NÚMEROS!!!")

                cidade = input("Em qual cidade essa pessoa mora:\n-> ")
                while (cidade.strip() == ""):
                    cidade = input("Em qual cidade essa pessoa mora:\n-> ")

                if CPF in pessoas:
                    print("USUÁRIO JÁ CADASTRADo!!!")
                    continue
                elif (CPFValidado == True):
                    pessoas[CPF] = {"nome":nome, "idade": idade, "cidade": cidade}
                
            elif (opcao == 2):
                for CPF in pessoas:
                    print(f"CPF: {CPF}")
                    print(f"NOME: {pessoas[CPF]['nome']}")
                    print(f"IDADE: {pessoas[CPF]['idade']}")
                    print(f"CIDADE: {pessoas[CPF]['cidade']}")
                    print("---------------------------------------------")

            elif (opcao == 3): 
                try:
                    CPF = (int(input("Digite o CPF (SEM TRAÇOS OU PONTOS): ")))
                    CPF = str(CPF)
                    if (len(CPF) == 11):
                        if CPF in pessoas:
                            print(f"CPF: {CPF}")
                            print(f"NOME: {pessoas[CPF]['nome']}")
                            print(f"IDADE: {pessoas[CPF]['idade']}")
                            print(f"CIDADE: {pessoas[CPF]['cidade']}")
                        else:
                            print("USUÁRIO NÃO CADASTRADO!!!")
                    else:
                        print("O CPF É INVÁLIDO, POIS ELE DEVE CONTER EXATAMENTE 11 DIGITOS!!!")
                except ValueError:
                    print("DIGITE APENAS NÚMEROS!!!")
            elif (opcao == 4):
                try:
                    CPF = (int(input("Digite o CPF (SEM TRAÇOS OU PONTOS): ")))
                    CPF = str(CPF)
                    if (len(CPF) == 11):
                        if CPF in pessoas:
                            print(f"CPF: {CPF}")
                            print(f"NOME: {pessoas[CPF]['nome']}")
                            print(f"IDADE: {pessoas[CPF]['idade']}")
                            print(f"CIDADE: {pessoas[CPF]['cidade']}")
                            nome = input("Digite o nome da pessoa:\n-> ")
                            while (nome.strip() == ""):
                                print("NOME INVÁLIDO!!!")
                                nome = input("Digite o nome da pessoa:\n-> ")
                            valido = False
                            while (valido == False):
                                try:
                                    idade = (int(input("Digite a idade dessa pessoa:\n-> ")))
                                    while (idade <= 0):
                                        print("IDADE INVÁLIDA!!!")
                                        idade = (int(input("Digite a idade dessa pessoa:\n-> ")))
                                    valido = True
                                except ValueError:
                                    print("DIGITE APENAS NÚMEROS!!!")

                            cidade = input("Em qual cidade essa pessoa mora:\n-> ")
                            while (cidade.strip() == ""):
                                cidade = input("Em qual cidade essa pessoa mora:\n-> ")

                        else:
                            print("USUÁRIO NÃO CADASTRADO!!!")
                    else:
                        print("O CPF É INVÁLIDO, POIS ELE DEVE CONTER EXATAMENTE 11 DIGITOS!!!")
                except ValueError:
                    print("DIGITE APENAS NÚMEROS!!!")

                pessoas[CPF]["nome"] = nome
                pessoas[CPF]["idade"] = idade
                pessoas[CPF]["cidade"] = cidade

            elif (opcao == 5):
                print("OK!!!\nFOI ÓTIMO TER VOCÊ CONOSCO!!!")
                encerrarSessao = True
        else:
            print("DIGITE 1, 2, 3, 4 OU 5!!!")

    except ValueError:
        print("DIGITE APENAS NÚMEROS!!!")
