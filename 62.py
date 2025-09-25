# 62. Crie um sistema de gerenciamento de biblioteca com busca avançada, empréstimos e controle de multas usando listas e tuplas.
# Lista de livros: (título, autor, ano, gênero, status)
livros = [
    ("Dom Casmurro", "Machado de Assis", 1899, "Romance", "DISPONÍVEL"),
    ("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, "Infantil", "DISPONÍVEL"),
    ("1984", "George Orwell", 1949, "Distopia", "DISPONÍVEL"),
    ("Capitães da Areia", "Jorge Amado", 1937, "Romance", "DISPONÍVEL"),
    ("A Revolução dos Bichos", "George Orwell", 1945, "Sátira", "DISPONÍVEL"),
    ("Grande Sertão: Veredas", "João Guimarães Rosa", 1956, "Romance", "DISPONÍVEL"),
    ("Memórias Póstumas de Brás Cubas", "Machado de Assis", 1881, "Romance", "DISPONÍVEL"),
    ("Ensaio sobre a Cegueira", "José Saramago", 1995, "Ficção", "DISPONÍVEL"),
    ("O Hobbit", "J.R.R. Tolkien", 1937, "Fantasia", "DISPONÍVEL"),
    ("Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997, "Fantasia", "DISPONÍVEL")
]

# Lista de usuários: (nome, livros_emprestados)
usuarios = [
    ("Ana", []),
    ("Carlos", []),
    ("Mariana", []),
    ("João", []),
    ("Beatriz", []),
    ("Rafael", []),
    ("Fernanda", []),
    ("Lucas", []),
    ("Juliana", []),
    ("Mateus", [])
]


# Lista de empréstimos: (nome do cliente, nome do livro, data_emprestimo, data_devolucao)
emprestimos = []


print("SEJA MUITO BEM-VINDO(A) AO SISTEMA DE GERENCIAMENTO BIBLIOTECÁRIO DO CÁSSIO!!!")
encerrarSessao = False
while encerrarSessao == False:
    try:
        print("<------------------------------------------------------------------------------>")
        opcao = int(input("O que deseja fazer?\nDigite:\n01- Listar Livros;\n02- Inserir Livro;\n03- Excluir Livro;\n04- Atualizar Livro;\n05- Listar Clientes;\n06- Cadastrar Cliente;\n07- Excluir Cliente\n08- Atualizar Cliente\n09- Visualizar Empréstimos;\n10- Cadastrar Empréstimo de Livro;\n11- Cadastrar Devolução de Livro;\n12- Buscar Obra;\n13- Encerrar Sessão.\n-> "))
        if (1 <= opcao <= 13):
            print("OPÇÃO VÁLIDA!!!")
            # idLivro += 1
            # Listar Livros:
            if (opcao == 1):
                ID = 1
                print("LIVROS:")
                for livro in livros:
                    print("ID:{} | Título: {} | Autor: {} | Ano de Publicação: {} | Gênero do Livro: {} | Situação de Emprestimo: {}".format(ID, livro[0], livro[1], livro[2], livro[3], livro[4]))
                    ID += 1

            # Inserir um livro:
            elif (opcao == 2):
                valido = False
                while (valido == False):
                    nome = input("Digite o nome do livro:\n-> ")
                    while (nome.strip() == ""):
                        nome = input("Digite o nome do livro:\n-> ")
                    autor = input("Digite o nome do autor:\n-> ")
                    while (autor.strip() == ""):
                        autor = input("Digite o nome do autor:\n-> ")
                    anoValido = False
                    while (anoValido == False):
                        try:
                            ano = (int(input("Digite o ano de publicação da obra:\n-> ")))
                            anoValido = True
                        except ValueError:
                            print("Digite apenas numeros!!!")
                    genero = input("Digite o gênero do livro:\n-> ")
                    while (genero.strip() == ""):
                        genero = input("Digite o gênero do livro:\n-> ")
                    valido = True
                livros.append((nome, autor, ano, genero, "DISPONÍVEL"))
                # print(livros)

            # Excluir livro:
            elif (opcao == 3):
                IDValido = False
                while (IDValido == False):
                    try:
                        excluir = (int(input("Digite o ID do livro que deseja excluir:\n-> ")))
                        excluir = (excluir - 1)
                        if (0 <= excluir < (len(livros))):
                            print("ID válido!!!")
                            # idLivro -= 1
                            IDValido = True
                        else:
                            print("ID inválido!!!")
                    except ValueError:
                        print("Digite apenas numeros!!!")
                del livros[excluir]
                # print(livros)
            
            # Atualizar livro:
            elif (opcao == 4):
                IDValido = False
                while (IDValido == False):
                    try:
                        atualizar = (int(input("Digite o ID do livro que deseja atualizar:\n-> ")))
                        atualizar = (atualizar - 1)
                        if (0 <= atualizar < (len(livros))):
                            print("ID válido!!!")
                            IDValido = True
                            valido = False
                            while (valido == False):
                                nomeAtualizado = input("Digite o nome do livro:\n-> ")
                                while (nomeAtualizado.strip() == ""):
                                    nomeAtualizado = input("Digite o nome do livro:\n-> ")
                                autorAtualizado = input("Digite o nome do autor:\n-> ")
                                while (autorAtualizado.strip() == ""):
                                    autorAtualizado = input("Digite o nome do autor:\n-> ")
                                anoValido = False
                                while (anoValido == False):
                                    try:
                                        anoAtualizado = (int(input("Digite o ano de publicação da obra:\n-> ")))
                                        anoValido = True
                                    except ValueError:
                                        print("Digite apenas numeros!!!")
                                generoAtualizado = input("Digite o gênero do livro:\n-> ")
                                while (generoAtualizado.strip() == ""):
                                    generoAtualizado = input("Digite o gênero do livro:\n-> ")
                                valido = True
                                livros[atualizar] = ((nomeAtualizado, autorAtualizado, anoAtualizado, generoAtualizado, "DISPONÍVEL"))
                        else:
                            print("ID inválido!!!")
                    except ValueError:
                        print("Digite apenas numeros!!!")

            # Listar Clientes:
            elif (opcao == 5):
                print("CLIENTES:")
                ID = 1
                for pessoa in usuarios:
                    print("ID:{} | Nome: {} | Empréstimos: {} ".format(ID, pessoa[0], pessoa[1]))
                    ID += 1

            # Cadastrar Cliente:
            elif (opcao == 6):
                valido = False
                while (valido == False):
                    nome = input("Digite o nome do cliente:\n-> ")
                    while (nome.strip() == ""):
                        nome = input("Digite o nome do cliente:\n-> ")
                    valido = True
                usuarios.append((nome, []))

            # Excluir Cliente:
            elif (opcao == 7):
                IDValido = False
                while (IDValido == False):
                    try:
                        excluir = (int(input("Digite o ID do cliente que deseja excluir:\n-> ")))
                        excluir = (excluir - 1)
                        if (0 <= excluir <= (len(usuarios))):
                            print("ID válido!!!")
                            IDValido = True
                        else:
                            print("ID inválido!!!")
                    except ValueError:
                        print("Digite apenas numeros!!!")
                del usuarios[excluir]

            # Atualizar Cliente:
            elif (opcao == 8):
                IDValido = False
                while (IDValido == False):
                    try:
                        atualizar = (int(input("Digite o ID do cliente que deseja atualizar:\n-> ")))
                        atualizar = (atualizar - 1)
                        if (0 <= atualizar < (len(usuarios))):
                            print("ID válido!!!")
                            IDValido = True
                            valido = False
                            while (valido == False):
                                nomeAtualizado = input("Digite o nome do cliente:\n-> ")
                                while (nomeAtualizado.strip() == ""):
                                    nomeAtualizado = input("Digite o nome do cliente:\n-> ")
                                valido = True
                                usuarios[atualizar] = ((nomeAtualizado, []))
                        else:
                            print("ID inválido!!!")
                    except ValueError:
                        print("Digite apenas numeros!!!")

            # Visualizar Empréstimo:
            elif (opcao == 9):
                ID = 1
                print("EMPRÉSTIMOS:")
                for emprestimo in emprestimos:
                    print("ID DO EMPRÉSTIMO: {} | Cliente: {} | Livro: {} | Data do Empréstimo: {} | Data de Devolução: {}".format(ID ,emprestimo[0], emprestimo[1], emprestimo[2], emprestimo[3]))
                    ID += 1
            
            # Cadastrar Empréstimo:
            elif (opcao == 10):
                IDClienteValido = False
                IDLivroValido = False
                while ((IDClienteValido == False) or (IDLivroValido == False)):
                    while (IDClienteValido == False):
                        try:
                            IDCliente = (int(input("Digite o ID do cliente que fez o empréstimo do livro:\n-> ")))
                            IDCliente = (IDCliente - 1)
                            if (0 <= IDCliente < (len(usuarios))):
                                print("ID do cliente válido!!!")
                                IDClienteValido = True
                                while (IDLivroValido == False):
                                    try:
                                        IDLivro = (int(input("Digite o ID do livro que o cliente fez o empréstimo:\n-> ")))
                                        IDLivro = (IDLivro - 1)
                                        if (0 <= IDLivro <= (len(usuarios))):
                                            print("ID do livro válido!!!")
                                            IDLivroValido = True
                                    except ValueError:
                                        print("Digite apenas números!!!")
                            else:
                                print("ID do cliente inválido!!!")
                        except ValueError:
                            print("Digite apenas números!!!")

                # Adicionando informação no lista clientes
                usuarios[IDCliente][IDLivroValido].extend([livros[IDLivro][0]])


                # Looping para verificar a coerência das informações:
                verificado = False
                while (verificado == False):
                    diaI = (int(input("Digite o dia que o cliente pegou o livro: ")))
                    mesI = (int(input("Digite o mês que o cliente pegou o livro: ")))
                    anoI = (int(input("Digite o ano que o cliente pegou o livro: ")))

                    diaF = (int(input("Digite o dia que o cliente deve devolver o livro: ")))
                    mesF = (int(input("Digite o mês que o cliente deve devolver o livro: ")))
                    anoF = (int(input("Digite o ano que o cliente deve devolver o livro: ")))

                    dataDeEmprestimo = ("válida")
                    if ((diaI <= 30) and (mesI == 4 or mesI == 6 or mesI == 9 or mesI == 11)):
                        dataDeEmprestimo = ("válida")
                    elif (diaI <= 31) and (mesI == 1 or mesI == 3 or mesI == 5 or mesI == 7 or mesI == 8 or mesI == 10 or mesI == 12):
                        dataDeEmprestimo = ("válida")
                    elif ((diaI <= 29) and (mesI == 2)and ((anoI % 400 == 0) or (anoI % 4 == 0 and anoI % 100 != 0))):
                        dataDeEmprestimo = ("válida")
                    elif ((diaI <= 28) and (mesI == 2) and ((anoI % 400 != 0) or (anoI % 4 == 0 and anoI % 100 != 0))):
                        dataDeEmprestimo = ("válida")
                    else:
                        dataDeEmprestimo = ("inválida")

                    dataDeDevolucao = ("válida")
                    if ((diaF <= 30) and (mesF == 4 or mesF == 6 or mesF == 9 or mesF == 11)):
                        dataDeDevolucao = ("válida")
                    elif (diaF <= 31) and (mesF == 1 or mesF == 3 or mesF == 5 or mesF == 7 or mesF == 8 or mesF == 10 or mesF == 12):
                        dataDeDevolucao = ("válida")
                    elif ((diaF <= 29) and (mesF == 2)and ((anoF % 400 == 0) or (anoF % 4 == 0 and anoF % 100 != 0))):
                        dataDeDevolucao = ("válida")
                    elif ((diaF <= 28) and (mesF == 2) and ((anoF % 400 != 0) or (anoF % 4 == 0 and anoF % 100 != 0))):
                        dataDeDevolucao = ("válida")
                    else:
                        dataDeDevolucao = ("inválida")

                    if (dataDeEmprestimo == ("válida") and dataDeDevolucao == ("válida") and (anoI <= anoF)):
                        verificado = True
                    elif (dataDeDevolucao == "inválida"):
                        print("A data {}/{}/{} NÃO É VÁLIDA!!!".format(diaF, mesF, anoF))
                    elif (dataDeEmprestimo == "inválida"):
                        print("A data {}/{}/{} NÃO É VÁLIDA!!!".format(diaI, mesI, anoI))
                    elif (anoI > anoF):
                        print("Ano de entrega inválido!!! O ano de entrega não pode ser maior que o de empréstimo!!!")

                # Adicionando informação nos emprestimos:
                nomeCliente = usuarios[IDCliente][0]
                nomeLivro = livros[IDLivro][0]
                dataEmprestimo = ("{}/{}/{}".format(diaI, mesI, anoI))
                dataDevolucao = ("{}/{}/{}".format(diaF, mesF, anoF))
                emprestimos.append((nomeCliente, nomeLivro, dataEmprestimo, dataDevolucao))

                # Atualizando a situação do livro:
                # ("Dom Casmurro", "Machado de Assis", 1899, "Romance", "DISPONÍVEL")
                autorLivro = livros[IDLivro][1]
                anoPublicacao = livros[IDLivro][2]
                genero = livros[IDLivro][3]
                livros[IDLivro] = ((nomeLivro, autorLivro, anoPublicacao, genero, "INDISPONÍVEL"))

            # Cadastrar devolução da obra:
            elif (opcao == 11):
                IDEmprestimoValido = False
                while (IDEmprestimoValido == False):
                    try:
                        IDDoEmprestimo = (int(input("Digite o ID do empréstimo do livro:\n-> ")))
                        IDDoEmprestimo = (IDDoEmprestimo - 1)
                        if (0 <= IDDoEmprestimo < (len(usuarios))):
                            print("ID do emprestimo válido!!!")
                            IDEmprestimoValido = True
                            if (livros[IDDoEmprestimo][4] == "INDISPONÍVEL"):
                                verificado = False
                                while (verificado == False):
                                    diaD = (int(input("Digite o dia que o cliente devolveu o livro: ")))
                                    mesD = (int(input("Digite o mês que o cliente devolveu o livro: ")))
                                    anoD = (int(input("Digite o ano que o cliente devolveu o livro: ")))

                                    dataDeDevolucao = ("válida")
                                    if ((diaD <= 30) and (mesD == 4 or mesD == 6 or mesD == 9 or mesD == 11)):
                                        dataDeDevolucao = ("válida")
                                    elif (diaD <= 31) and (mesD == 1 or mesD == 3 or mesD == 5 or mesD == 7 or mesD == 8 or mesD == 10 or mesD == 12):
                                        dataDeDevolucao = ("válida")
                                    elif ((diaD <= 29) and (mesD == 2)and ((anoD % 400 == 0) or (anoD % 4 == 0 and anoD % 100 != 0))):
                                        dataDeDevolucao = ("válida")
                                    elif ((diaD <= 28) and (mesD == 2) and ((anoD % 400 != 0) or (anoD % 4 == 0 and anoD % 100 != 0))):
                                        dataDeDevolucao = ("válida")
                                    else:
                                        dataDeDevolucao = ("inválida")

                                    if (dataDeDevolucao == ("válida")):
                                        verificado = True
                                    else:
                                        print("A data {}/{}/{} NÃO É VÁLIDA!!!".format(diaF, mesF, anoF))

                                    dataDeEmprestimoEsperada = emprestimos[IDDoEmprestimo][3]
                                    diaEstimado = ("{}{}".format(dataDeEmprestimoEsperada[0], dataDeEmprestimoEsperada[1]))
                                    diaEstimado = (int(diaEstimado))
                                    mesEstimado = ("{}{}".format(dataDeEmprestimoEsperada[3], dataDeEmprestimoEsperada[4]))
                                    mesEstimado = (int(mesEstimado))
                                    anoEstimado = ("{}{}{}{}".format(dataDeEmprestimoEsperada[6], dataDeEmprestimoEsperada[7], dataDeEmprestimoEsperada[8], dataDeEmprestimoEsperada[9]))
                                    anoEstimado = (int(anoEstimado))

                                    if ((diaD > diaEstimado) or (mesD > mesEstimado) or (anoD > anoEstimado)):
                                        print("O cliente devolveu o livro com atraso!!!")
                                        print("A data de devolução era: {}/{}/{}!!!".format(diaEstimado, mesEstimado, anoEstimado))

                            else:
                                print("O livro não foi emprestado!!!")
                        else:
                            print("ID do cliente inválido!!!")
                    except ValueError:
                        print("Digite apenas números!!!")

            # Buscar Obra:
            elif (opcao == 12):
                valido = False
                while (valido == False):
                    try:
                        opcao = (int(input("Você deseja filtrar a obra pelo:\nDigite:\n1- Autor;\n2- Ano de publicação;\n3- Gênero.\n-> ")))
                        if (1 <= opcao <= 3):
                            print("Opção válida!!!")
                            valido = True
                        else:
                            print("Opção inválida!!! Digite 1, 2 ou 3")
                    except ValueError:
                        print("Digite apenas números!!!")

                if (opcao == 1):
                    autor = (input("Digite o nome do autor:\n-> "))
                    while (autor.strip() == ""):
                        autor = (input("Digite o nome do autor:\n-> "))
                    for livro in livros:
                        if (livro[1].lower() == autor.lower()):
                            print("Título: {} | Autor: {} | Ano de Publicação: {} | Gênero do Livro: {} | Situação de Emprestimo: {}".format(livro[0], livro[1], livro[2], livro[3], livro[4]))
                
                elif (opcao == 2):
                    valido = False
                    while (valido == False):
                        try:
                            ano = int(input("Digite o nome do autor:\n-> "))
                            while (ano <= 0):
                                ano = int(input("Digite o nome do autor:\n-> "))
                            valido = True
                            for livro in livros:
                                if (livro[2] == ano):
                                    print("Título: {} | Autor: {} | Ano de Publicação: {} | Gênero do Livro: {} | Situação de Emprestimo: {}".format
                                    (livro[0], livro[1], livro[2], livro[3], livro[4]))
                        except ValueError:
                            print("Digite apenas números!!!")

                elif (opcao == 3):
                    genero = (input("Digite o gênero da obra:\n-> "))
                    while (genero.strip() == ""):
                        genero = (input("Digite o gênero da obra:\n-> "))
                    for livro in livros:
                        if (livro[3].lower() == genero.lower()):
                            print("Título: {} | Autor: {} | Ano de Publicação: {} | Gênero do Livro: {} | Situação de Emprestimo: {}".format(livro[0], livro[1], livro[2], livro[3], livro[4]))

            # Finalizar Sessão:
            elif (opcao == 13):
                print("OK!!!")
                print("Foi ótimo ter você conosco!!!")
                encerrarSessao = True
        else:
            print("DIGITE 1, 2, 3, 4, 5, 6, 7 OU 8!!!")

    except ValueError:
        print("DIGITE APENAS NÚMEROS!!!")
