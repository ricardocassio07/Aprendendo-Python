# 55. Desenvolva um sistema de controle de estoque usando listas e tuplas com operações CRUD [Create (Criar), Read (Ler), Update (Atualizar) e Delete (Apagar)].
produto1 = ("maça", 30)
produto2 = ("pepino", 50)
produto3 = ("banana", 15)
produto4 = ("melancia", 30)
produto5 = ("pera", 28)
produtos = [produto1, produto2, produto3, produto4, produto5]
operacaoValidada = False
while (operacaoValidada == False):
    try:
        opcao = int(input("O que deseja fazer?\nDigite:\n1- Adicionar um produto;\n2- Ler produtos do estoque;\n3- Atualizar um produto;\n4- Deletar um produto.\n-> "))
        if (opcao == 1):
            nomeP6 = ""
            qtdP6 = ""
            while (nomeP6 == "" and qtdP6 == ""):
                nomeP6 = input("Digite o nome do produto: ")
                qtdP6 = int(input("Digite a quantidade do produto: "))
                produto6 = (nomeP6, qtdP6)
            produtos.append(produto6)
            print("Produto adicionado!")
            for i in range(len(produtos)):
                print("{} - {}".format(i, produtos[i]))
        elif (opcao == 2):
            for i in range(len(produtos)):
                print("{} - {}".format(i, produtos[i]))
        elif (opcao == 3):
            for i in range(len(produtos)):
                print("{} - {}".format(i, produtos[i]))
            id = int(input("Digite o número do produto que deseja atualizar: "))
            nome = input("Digite o novo nome: ")
            qtd = int(input("Digite a nova quantidade: "))
            produtoAtualizado = (nome, qtd)
            produtos[id] = produtoAtualizado
            print("Produto atualizado!")
            for i in range(len(produtos)):
                print("{} - {}".format(i, produtos[i]))
        elif opcao == 4:
            for i in range(len(produtos)):
                print("{} - {}".format(i, produtos[i]))
            id = int(input("Digite o número do produto que deseja deletar: "))
            produtos[id] = ("", 0)
            print("Produto deletado!")
            for i in range(len(produtos)):
                print("{} - {}".format(i, produtos[i]))
        else:
            print("Opção inválida!")
        operacaoValidada = True
    except ValueError:
        print("VOCÊ DEVE DIGITAR 1-Criar, 2-Ler, 3-Atualizar ou 4-Delestar!!!")