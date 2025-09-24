# 12. Crie um sistema de gerenciamento de biblioteca com busca avançada, empréstimos e controle de multas usando listas e tuplas.
# Lista de livros: (id, título, autor, ano, gênero, disponível)
livros = [
    ("Dom Casmurro", "Machado de Assis", 1899, "Romance", "DIPONÍVEL"),
    ("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, "Infantil", "DIPONÍVEL"),
    ("1984", "George Orwell", 1949, "Distopia", "DIPONÍVEL")
]

# Lista de usuários: (id, nome, livros_emprestados)
usuarios = [
    ("Ana", []),
    ("Carlos", []),
    ("Mariana", [])
]

# Lista de empréstimos: (id_usuario, id_livro, data_emprestimo, data_devolucao)
emprestimos = [
    # exemplo vazio, será preenchido quando houver empréstimo
]

# Último ID:
id = 3
# -------- COMECA DAQUI
encerrarSessao = False
while encerrarSessao == False:
    try:
        opcao = int(input("O que deseja fazer?\nDigite:\n1- Cadastrar pessoas;\n2- Listar pessoas;\n3- Buscar pessoas;\n4- Atualizar dados;\n5- Encerrar sessão.\n-> "))
        if (1 <= opcao <= 5):
            print("OPÇÃO VÁLIDA!!!")
            id += 1
            # Inserir um livro:
            if (opcao == 1):
                # print("-> DA ESQUERDA PARA A DIREITA, CONSIDERE QUE O ID DE CADA LIVRO COMEÇA EM 1 E SEGUE EM ORDEM CRESCENTE AUMENTANDO DE 1 EM 1!!! <-\n")
                ID = 1
                for livro in livros:
                    print("ID:{} | Título: {} | Autor: {} | Ano de Publicação: {} | Genêro do Livro: {} | Situação de Emprestimo: {}".format(ID, livro[0], livro[1], livro[2], livro[3], livro[4]))
                    ID += 1
                # print(livros)
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
                    genero = input("Digite o genêro do livro:\n-> ")
                    while (genero.strip() == ""):
                        genero = input("Digite o genêro do livro:\n-> ")
                    valido = True
                livros.append((id, nome, autor, ano, genero, "DISPONÍVEL"))
                # print(livros)
        else:
            print("DIGITE 1, 2, 3, 4 OU 5!!!")

    except ValueError:
        print("DIGITE APENAS NÚMEROS!!!")




# Excluir livro:
# print("-> DA ESQUERDA PARA A DIREITA, CONSIDERE QUE O ID DE CADA LIVRO COMEÇA EM 1 E SEGUE EM ORDEM CRESCENTE AUMENTANDO DE 1 EM 1!!! <-\n")
ID = 1
for livro in livros:
    print("ID:{} | Título: {} | Autor: {} | Ano de Publicação: {} | Genêro do Livro: {} | Situação de Emprestimo: {}".format(ID, livro[0], livro[1], livro[2], livro[3], livro[4]))
    ID += 1
# print(livros)
IDValido = False
while (IDValido == False):
    try:
        excluir = (int(input("Digite o ID do livro que deseja excluir:\n-> ")))
        excluir = (excluir - 1)
        if (0 <= excluir <= (id - 1)):
            print("ID válido!!!")
            id -= 1
            IDValido = True
        else:
            print("ID inválido!!!")
    except ValueError:
        print("Digite apenas numeros!!!")
del livros[excluir]
# print(livros)

# Atualizar livro:
# print("-> DA ESQUERDA PARA A DIREITA, CONSIDERE QUE O ID DE CADA LIVRO COMEÇA EM 1 E SEGUE EM ORDEM CRESCENTE AUMENTANDO DE 1 EM 1!!! <-\n")
ID = 1
for livro in livros:
    print("ID:{} | Título: {} | Autor: {} | Ano de Publicação: {} | Genêro do Livro: {} | Situação de Emprestimo: {}".format(ID, livro[0], livro[1], livro[2], livro[3], livro[4]))
    ID += 1
# print(livros)
IDValido = False
while (IDValido == False):
    try:
        excluir = (int(input("Digite o ID do livro que deseja atualizar:\n-> ")))
        excluir = (excluir - 1)
        if (0 <= excluir <= (id - 1)):
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
                generoAtualizado = input("Digite o genêro do livro:\n-> ")
                while (generoAtualizado.strip() == ""):
                    generoAtualizado = input("Digite o genêro do livro:\n-> ")
                valido = True
                livros[excluir] = ((nomeAtualizado, autorAtualizado, anoAtualizado, generoAtualizado, "DISPONÍVEL"))
        else:
            print("ID inválido!!!")
    except ValueError:
        print("Digite apenas numeros!!!")
# print(livros)
ID = 1
for livro in livros:
    print("ID:{} | Título: {} | Autor: {} | Ano de Publicação: {} | Genêro do Livro: {} | Situação de Emprestimo: {}".format(ID, livro[0], livro[1], livro[2], livro[3], livro[4]))
    ID += 1