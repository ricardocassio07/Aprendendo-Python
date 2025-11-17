'''
   Desenvolva um Sistema de Gerenciamento de Biblioteca Digital que integre todos os conceitos fundamentais do Python:
    -> Range: Para paginação, numeração e iterações controladas;   
    -> For: Para percorrer coleções e processar dados;
    -> Funções: Para modularizar o código e reutilizar funcionalidades;
    -> Arquivos: Para persistir dados em JSON e gerar relatórios;
    -> Tuplas: Para armazenar dados imutáveis como coordenadas e configurações;
    -> Dicionários: Para estruturar informações complexas de livros e usuários.
    
   O sistema deve permitir:
    -> Cadastro e gerenciamento de livros;
    -> Cadastro e gerenciamento de usuários;
    -> Sistema de empréstimos e devoluções;
    -> Busca avançada com filtros;
    -> Persistência de dados em arquivos;
    -> Interface interativa com menus paginados.
'''
# Dicionário que armazena vetores, sendo cada um deles responsável por armazenar as obras em ordem alfabética, sendo o primeiro resposável por armazenar as obras com que se iniciam com a letra 'a' e o penúltimo com a letra 'z', o último vetor irá armazenar as obras com início numérico:

letras = [
    "A","B","C","D","E","F","G","H","I","J","K","L","M",
    "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
]
obras = {
    "A": [("A Revolução dos Bichos", "George Orwell", 1945, "Sátira", "DISPONÍVEL")],
    "B": [],
    "C": [("Capitães da Areia", "Jorge Amado", 1937, "Romance", "DISPONÍVEL")],
    "D": [("Dom Casmurro", "Machado de Assis", 1899, "Romance", "DISPONÍVEL")],
    "E": [("Ensaio sobre a Cegueira", "José Saramago", 1995, "Ficção", "DISPONÍVEL")],
    "F": [],
    "G": [("Grande Sertão: Veredas", "João Guimarães Rosa", 1956, "Romance", "DISPONÍVEL")],
    "H": [("Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997, "Fantasia", "DISPONÍVEL")],
    "I": [],
    "J": [],
    "K": [],
    "L": [],
    "M": [("Memórias Póstumas de Brás Cubas", "Machado de Assis", 1881, "Romance", "DISPONÍVEL")],
    "N": [],
    "O": [("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, "Infantil", "DISPONÍVEL"), ("O Hobbit", "J.R.R. Tolkien", 1937, "Fantasia", "DISPONÍVEL")],
    "P": [],
    "Q": [],
    "R": [],
    "S": [],
    "T": [],
    "U": [],
    "V": [],
    "W": [],
    "X": [],
    "Y": [],
    "Z": [],
    "NUM": [("1984", "George Orwell", 1949, "Distopia", "DISPONÍVEL")]
}
usuarios = {
    "A": [],
    "B": [],
    "C": [],
    "D": [],
    "E": [],
    "F": [],
    "G": [],
    "H": [],
    "I": [],
    "J": [],
    "K": [],
    "L": [],
    "M": [],
    "N": [],
    "O": [],
    "P": [],
    "Q": [],
    "R": [],
    "S": [],
    "T": [],
    "U": [],
    "V": [],
    "W": [],
    "X": [],
    "Y": [],
    "Z": []
}

emprestimos = []


def verificar():             
    verificado = False
    while (verificado == False):
        try:
            continuarNaSecao = (int(input(
            "DIGITE:\n"\
            "1- SIM\n"\
            "2- NÃO\n"\
            "-> "
            )))
            if (1 <= continuarNaSecao <= 2):
                verificado = True
                if (continuarNaSecao == 2):
                    return False
                else:
                    return True
            else:
                print("-> DESEJO INVÁLIDO <-")
        except ValueError:
            print("-> DIGITE APENAS NÚMEROS! <-")


print("----------- SISTEMA BIBLIOTECÁRIO -----------")
print("---------- SEJA MUITO BEM-VINDO(A) ----------")
continuar_no_sistema = True
while (continuar_no_sistema == True):
    verificado = False
    print("---------------------------------------------")
    while (verificado == False):
        try:
            desejo = (int(input("O QUE DESEJA:\n"\
            "DIGITE:\n"\
            "1- GERENCIAR OBRAS CATÁLOGADAS\n"\
            "2- GERENCIAR USUÁRIOS CADASTRADOS\n"\
            "3- GERENCIAR EMPRÉSTIMOS\n"\
            "9- ENCERRAR SISTEMA\n"\
            "-> "
            )))
            if ((1 <= desejo <= 3) or (desejo == 9)):
                verificado = True
            else:
                print("-> DESEJO INVÁLIDO <-")
        except ValueError:
            print("-> DIGITE APENAS NÚMEROS! <-")


    if (1 <= desejo <= 3):
        # Gerenciar obras:
        if (desejo == 1):
            print("----------- GERENCIADOR DE OBRAS -----------")
            continuarGerenciarObras = True
            while (continuarGerenciarObras == True):
                verificado = False
                while (verificado == False):
                    try:
                        desejoObra = (int(input("O QUE DESEJA:\n"\
                        "DIGITE:\n"\
                        "1- VISUALIZAR OBRAS CADASTRADAS\n"\
                        "2- CADASTRAR OBRA\n"\
                        "3- MODIFICAR AS INFORMAÇÕES DE ALGUMA OBRA\n"\
                        "4- EXCLUIR OBRA\n"\
                        "-> "
                        )))
                        if (1 <= desejoObra <= 6):
                            verificado = True
                        else:
                            print("-> DESEJO INVÁLIDO <-")
                    except ValueError:
                        print("-> DIGITE APENAS NÚMEROS! <-")
                
                
                if (desejoObra == 1):
                    # Mostrar obras catálogadas
                    print("--------------- MOSTRAR OBRA ---------------")
                    continuarMostrarObras = True
                    while (continuarMostrarObras == True):
                        verificado = False
                        while (verificado == False):
                            try:
                                opcao = (int(input("QUAL CATEGORIA DESEJA VISUALIZAR?\nDIGITE:\n1- À PARTIR DA LETRA INICIAL DA OBRA\n2- À PARTIR DO AUTOR\n3- À PARTIR DO ANO DE PUBLICAÇÃO\n4- À PARTIR DO GÊNERO\n5- LIVROS INICIADOS COM NÚMERO\n6- BUSCAR POR UMA OBRA ESPECÍFICA\n-> ")))
                                if (1 <= opcao <= 4):
                                    verificado = True
                                else:
                                    print("-> DESEJO INVÁLIDO <-")
                            except ValueError:
                                print("-> DIGITE APENAS NÚMEROS! <-")

                        # 1- À PARTIR DA LETRA INICIAL DA OBRA:
                        if (opcao == 1):
                            verificado = False
                            while (verificado == False):
                                letra = (input("DIGITE A LETRA:\n-> "))
                                # Ajustando a letra para minúsculo:
                                letra = letra.upper()
                                if (letra in letras):
                                    verificado = True
                                else:
                                    print("-> DESEJO INVÁLIDO <-")

                            if len(obras[letra]) == 0:
                                print("-> AINDA NÃO FORAM CADASTRADAS NENHUMA OBRA <-")
                            else:
                                for obra in obras[letra]:
                                    print("----------------------------------------------")
                                    print("NOME: {}".format(obra[0]))
                                    print("AUTOR: {}".format(obra[1]))
                                    print("ANO: {}".format(obra[2]))
                                    print("GÊNERO: {}".format(obra[3]))
                                    print("DISPONIBILIDADE PARA EMPRÉSTIMO: {}".format(obra[4]))

                        # 2- À PARTIR DO AUTOR:
                        elif (opcao == 2):
                            verificado = False
                            while (verificado == False):
                                autor = (input("DIGITE O NOME DO(A) AUTOR(A):\n-> "))
                                autor = autor.strip()
                                if (len(autor) > 0):
                                    verificado = True
                                else:
                                    print("-> DESEJO INVÁLIDO <-")

                            if len(obras[letra]) == 0:
                                print("-> AINDA NÃO FORAM CADASTRADAS NENHUMA OBRA <-")
                            else:
                                for inicial in obras:
                                    for obra in obras[inicial]:
                                        if (obra[1] == autor):
                                            print("----------------------------------------------")
                                            print("NOME: {}".format(obra[0]))
                                            print("AUTOR: {}".format(obra[1]))
                                            print("ANO: {}".format(obra[2]))
                                            print("GÊNERO: {}".format(obra[3]))
                                            print("DISPONIBILIDADE PARA EMPRÉSTIMO: {}".format(obra[4]))

                        # 3- À PARTIR DO ANO DE PUBLICAÇÃO DA OBRA:
                        elif (opcao == 3):
                            verificado = False
                            while (verificado == False):
                                try:
                                    ano = (input("DIGITE O ANO DE LANÇAMENTO DA OBRA:\n-> "))
                                    ano = ano.strip()
                                    ano = int(ano)
                                    if (ano > 0):
                                        verificado = True
                                    else:
                                        print("-> DESEJO INVÁLIDO <-")
                                except:
                                    print("-> DIGITE APENAS NÚMEROS <-")

                            if len(obras[letra]) == 0:
                                print("-> AINDA NÃO FORAM CADASTRADAS NENHUMA OBRA <-")
                            else:
                                for inicial in obras:
                                    for obra in obras[inicial]:
                                        if (obra[2] == ano):
                                            print("----------------------------------------------")
                                            print("NOME: {}".format(obra[0]))
                                            print("AUTOR: {}".format(obra[1]))
                                            print("ANO: {}".format(obra[2]))
                                            print("GÊNERO: {}".format(obra[3]))
                                            print("DISPONIBILIDADE PARA EMPRÉSTIMO: {}".format(obra[4]))

                        # 4- À PARTIR DO GÊNERO
                        elif (opcao == 4):
                            verificado = False
                            while (verificado == False):
                                genero = (input("DIGITE O GÊNERO DA OBRA:\n-> "))
                                genero = genero.strip()
                                if (len(genero) > 0):
                                    verificado = True
                                else:
                                    print("-> DESEJO INVÁLIDO <-")

                            if len(obras[letra]) == 0:
                                print("-> AINDA NÃO FORAM CADASTRADAS NENHUMA OBRA <-")
                            else:
                                for inicial in obras:
                                    for obra in obras[inicial]:
                                        if (obra[3] == genero):
                                            print("----------------------------------------------")
                                            print("NOME: {}".format(obra[0]))
                                            print("AUTOR: {}".format(obra[1]))
                                            print("ANO: {}".format(obra[2]))
                                            print("GÊNERO: {}".format(obra[3]))
                                            print("DISPONIBILIDADE PARA EMPRÉSTIMO: {}".format(obra[4]))

                        # 5- LIVROS INICIADOS COM NÚMERO
                        elif (opcao == 5):
                            if len(obras[letra]) == 0:
                                print("-> AINDA NÃO FORAM CADASTRADAS NENHUMA OBRA <-")
                            else:
                                for obra in obras["NUM"]:
                                    print("----------------------------------------------")
                                    print("NOME: {}".format(obra[0]))
                                    print("AUTOR: {}".format(obra[1]))
                                    print("ANO: {}".format(obra[2]))
                                    print("GÊNERO: {}".format(obra[3]))
                                    print("DISPONIBILIDADE PARA EMPRÉSTIMO: {}".format(obra[4]))

                        # 6- BUSCAR POR UMA OBRA ESPECÍFICA
                        elif (opcao == 6):
                            verificado = False
                            while (verificado == False):
                                nomeObra = (input("DIGITE O NOME DA OBRA:\n-> "))
                                nomeObra = nomeObra.strip()
                                nomeObra = nomeObra.lower()
                                if (len(nomeObra) > 0):
                                    verificado = True
                                else:
                                    print("-> DESEJO INVÁLIDO <-")

                            if len(obras[letra]) == 0:
                                print("-> AINDA NÃO FORAM CADASTRADAS NENHUMA OBRA <-")
                            else:
                                for inicial in obras:
                                    for obra in obras[inicial]:
                                        if (((obra[0]).lower()) == nomeObra):
                                            print("----------------------------------------------")
                                            print("NOME: {}".format(obra[0]))
                                            print("AUTOR: {}".format(obra[1]))
                                            print("ANO: {}".format(obra[2]))
                                            print("GÊNERO: {}".format(obra[3]))
                                            print("DISPONIBILIDADE PARA EMPRÉSTIMO: {}".format(obra[4]))

                        print("VOCÊ DESEJA CONTINUAR BUSCANDO POR ALGUMA OBRA CATÁLOGADA:")
                        continuarMostrarObras = verificar()



                        
                elif (desejoObra == 2):
                    # INSERIR OBRA
                    print("--------------- INSERIR OBRA ---------------")
                    continuarInserirObras = True
                    while (continuarInserirObras ==True):
                        verificado = False
                        while (verificado == False):
                            nomeObra = (input("INSIRA O NOME DA OBRA:\n-> "))
                            nomeObra = nomeObra.strip()
                            if (len(nomeObra) > 0):
                                verificado = True
                            else:
                                print("-> NOME DA OBRA INVÁLIDO <-")

                        verificado = False
                        while (verificado == False):
                            nomeAutor = (input("INSIRA O NOME DO(A) AUTOR(A):\n-> "))
                            nomeAutor = nomeAutor.strip()
                            if (len(nomeAutor) > 0):
                                verificado = True
                            else:
                                print("-> NOME DO(A) AUTOR(A) INVÁLIDO <-")

                        verificado = False
                        while (verificado == False):
                            try:
                                ano = (input("DIGITE O ANO DE LANÇAMENTO DA OBRA:\n-> "))
                                ano = ano.strip()
                                ano = int(ano)
                                if (ano > 0):
                                    verificado = True
                                else:
                                    print("-> DESEJO INVÁLIDO <-")
                            except:
                                print("-> DIGITE APENAS NÚMEROS <-")

                        verificado = False
                        while (verificado == False):
                            genero = (input("DIGITE O GÊNERO DA OBRA:\n-> "))
                            genero = genero.strip()
                            if (len(genero) > 0):
                                verificado = True
                            else:
                                print("-> DESEJO INVÁLIDO <-")


                        obra = (nomeObra, nomeAutor, ano, genero, "DISPONÍVEL")
                        print(obra)
                        # print(obra[0])
                        for inicial in obras:
                            if (inicial.upper() in letras):
                                if ((nomeObra[0]) == (inicial.lower())):
                                    obras[inicial].append(obra)
                                    # print(obras[inicial])
                            else:
                                obras["NUM"].append(obra)
                                # print(obras["NUM"])
                        
                        print("VOCÊ DESEJA INSERIR MAIS ALGUMA OBRA:")
                        continuarInserirObras = verificar()
                    
                elif (desejoObra == 3):
                    # MODIFICAR OBRA
                    print("-------------- MODIFICAR OBRA --------------")
                    continuarModificarObras = True
                    while (continuarModificarObras == True):
                        verificado = False
                        while (verificado == False):
                            try:
                                opcao = (int(input("O TÍTULO DA OBRA COMEÇA COM UMA LETRA OU UM NÚMERO:\n"\
                                                   "DIGITE\n"\
                                                    "1- LETRA\n"\
                                                    "2- NÚMERO\n"\
                                                    "-> "
                                )))
                                if (1 <= opcao <= 2):
                                    verificado = True
                                else:
                                    print("-> OPÇÃO INVÁLIDA<-")
                            except:
                                print("-> DIGITE APENAS NÚMEROS <-")

                        if (opcao == 1):
                            verificado = False
                            while (verificado == False):
                                inicial = (input("DIGITE A LETRA INICIAL DA OBRA:\n-> "))
                                # Ajustando a letra para maiúsculo:
                                inicial = inicial.upper()
                                if (inicial in letras):
                                    verificado = True
                                else:
                                    print("-> DESEJO INVÁLIDO <-")
                        else:
                            inicial = ("NUM")

                        codigo = 0
                        if len(obras[inicial]) == 0:
                            print("-> AINDA NÃO FORAM CADASTRADAS NENHUMA OBRA <-")
                        else:
                            for obra in obras[inicial]:
                                codigo += 1
                                print("----------------------------------------------")
                                print("CÓDIGO: {}".format(codigo))
                                print("NOME: {}".format(obra[0]))
                                print("AUTOR: {}".format(obra[1]))
                                print("ANO: {}".format(obra[2]))
                                print("GÊNERO: {}".format(obra[3]))
                                print("DISPONIBILIDADE PARA EMPRÉSTIMO: {}".format(obra[4]))

                            verificado = False
                            while (verificado == False):
                                try:
                                    codigoObra = (int(input("DIGITE O CÓDIGO DA OBRA QUE DESEJA MODIFICAR DA OBRA:\n-> ")))
                                
                                    if (1 <= codigoObra <= codigo):
                                        verificado = True
                                    else:
                                        print("-> DESEJO INVÁLIDO <-")
                                except ValueError:
                                    print("-> DIGITE APENAS NÚMEROS <-")


                            for obra in obras[inicial]:
                                print(obra)
                                if ((obras[inicial].index(obra) + 1) == codigo):
                                    obraOriginal = obras[inicial][codigo - 1]
                                    print(obraOriginal)


                            verificado = False
                            while (verificado == False):
                                nomeAutor = (input("INSIRA O NOME DO(A) AUTOR(A):\n-> "))
                                nomeAutor = nomeAutor.strip()
                                if (len(nomeAutor) > 0):
                                    verificado = True
                                else:
                                    print("-> NOME DO(A) AUTOR(A) INVÁLIDO <-")

                            verificado = False
                            while (verificado == False):
                                try:
                                    ano = (input("DIGITE O ANO DE LANÇAMENTO DA OBRA:\n-> "))
                                    ano = ano.strip()
                                    ano = int(ano)
                                    if (ano > 0):
                                        verificado = True
                                    else:
                                        print("-> DESEJO INVÁLIDO <-")
                                except:
                                    print("-> DIGITE APENAS NÚMEROS <-")

                            verificado = False
                            while (verificado == False):
                                genero = (input("DIGITE O GÊNERO DA OBRA:\n-> "))
                                genero = genero.strip()
                                if (len(genero) > 0):
                                    verificado = True
                                else:
                                    print("-> DESEJO INVÁLIDO <-")


                            obraModificada = (obraOriginal[0], nomeAutor, ano, "DISPONÍVEL")
                            # print(obraModificada)

                            # Excluir o item original
                            del obras[inicial][codigoObra - 1]

                            # Inserir no lugar correto
                            obras[inicial].insert(codigoObra - 1, obraModificada)

                        
                    print("VOCÊ DESEJA MODIFICAR MAIS ALGUMA OBRA:")
                    continuarModificarObras = verificar()

                elif (desejoObra == 4):
                    # EXCLUIR OBRA
                    print("--------------- EXCLUIR OBRA ---------------")
                    continuarExcluirObras = True
                    while (continuarExcluirObras == True):
                        verificado = False
                        while (verificado == False):
                            try:
                                opcao = (int(input("O TÍTULO DA OBRA COMEÇA COM UMA LETRA OU UM NÚMERO:\n"\
                                                   "DIGITE\n"\
                                                    "1- LETRA\n"\
                                                    "2- NÚMERO\n"\
                                                    "-> "
                                )))
                                if (1 <= opcao <= 2):
                                    verificado = True
                                else:
                                    print("-> OPÇÃO INVÁLIDA<-")
                            except:
                                print("-> DIGITE APENAS NÚMEROS <-")

                        if (opcao == 1):
                            verificado = False
                            while (verificado == False):
                                inicial = (input("DIGITE A LETRA INICIAL DO NOME DA OBRA:\n-> "))
                                # Ajustando a letra para maiúsculo:
                                inicial = inicial.upper()
                                if (inicial in letras):
                                    verificado = True
                                else:
                                    print("-> DESEJO INVÁLIDO <-")
                        else:
                            inicial = ("NUM")
                        
                        codigo = 0
                        if len(obras[inicial]) == 0:
                            print("-> AINDA NÃO FORAM CADASTRADAS NENHUMA OBRA <-")
                        else:
                            for obra in obras[inicial]:
                                codigo += 1
                                print("----------------------------------------------")
                                print("CÓDIGO: {}".format(codigo))
                                print("NOME: {}".format(obra[0]))
                                print("AUTOR: {}".format(obra[1]))
                                print("ANO: {}".format(obra[2]))
                                print("GÊNERO: {}".format(obra[3]))
                                print("DISPONIBILIDADE PARA EMPRÉSTIMO: {}".format(obra[4]))

                            verificado = False
                            while (verificado == False):
                                try:
                                    codigoObra = (int(input("DIGITE O CÓDIGO DA OBRA QUE DESEJA MODIFICAR DA OBRA:\n-> ")))
                                
                                    if (1 <= codigoObra <= codigo):
                                        verificado = True
                                    else:
                                        print("-> DESEJO INVÁLIDO <-")
                                except ValueError:
                                    print("-> DIGITE APENAS NÚMEROS <-")


                        verificado = False
                        while (verificado == False):
                            try:
                                print("VOCÊ TEM CERTEZA QUE DESEJA EXCLUIR A OBRA:")
                                print("CÓDIGO: {}".format(codigoObra))
                                print("NOME: {}".format(obras[inicial][(codigoObra - 1)][0]))
                                print("AUTOR: {}".format(obras[inicial][(codigoObra - 1)][1]))
                                print("ANO: {}".format(obras[inicial][(codigoObra - 1)][2]))
                                print("GÊNERO: {}".format(obras[inicial][(codigoObra - 1)][3]))
                                print("DISPONIBILIDADE PARA EMPRÉSTIMO: {}".format(obras[inicial][(codigoObra - 1)][4]))
                                desejo = (int(input("DIGITE:\n1- SIM\n2- NÃO\n-> "
                                )))
                                if (1 <= desejo <= 2):
                                    verificado = True
                                    if (desejo == 1):
                                        del obras[inicial][codigoObra - 1]
                                else:
                                    print("-> OPÇÃO INVÁLIDA<-")
                            except:
                                print("-> DIGITE APENAS NÚMEROS <-")

                        print("VOCÊ DESEJA EXCLUIR MAIS ALGUMA OBRA:")
                        continuarExcluirObras = verificar()
                
                print("DESEJA CONTINUAR GERENCIANDO AS OBRAS:")
                continuarGerenciarObras = verificar()
                

        # Gerenciar usuários:
        elif (desejo == 2):
            print("---------- GERENCIADOR DE USUÁRIOS ----------")
            continuarGerenciarUsuarios = True
            while (continuarGerenciarUsuarios == True):
                verificado = False
                while (verificado == False):
                    try:
                        desejoUser = (int(input("O QUE DESEJA:\n"\
                        "DIGITE:\n"\
                        "1- VISUALIZAR USUÁRIOS CADASTRADAS\n"\
                        "2- CADASTRAR USUÁRIO\n"\
                        "3- MODIFICAR AS INFORMAÇÕES DE ALGUM USUÁRIO\n"
                        "-> "
                        )))
                        if (1 <= desejoUser <= 4):
                            verificado = True
                        else:
                            print("-> DESEJO INVÁLIDO <-")
                    except ValueError:
                        print("-> DIGITE APENAS NÚMEROS! <-")

                    
                if (desejoUser == 1):
                    # Mostrar usuários cadastrados
                    print("----------- USUÁRIOS CADASTRADOS -----------")
                    continuarVisualizarUsuarios = True
                    while (continuarVisualizarUsuarios == True):
                        verificado = False
                        while (verificado == False):
                            inicial = (input("DIGITE A LETRA INICIAL DO NOME DO USUÁRIO:\n-> "))
                            # Ajustando a letra para maiúsculo:
                            inicial = inicial.upper()
                            if (inicial in letras):
                                verificado = True
                            else:
                                print("-> DESEJO INVÁLIDO <-")

                        codigo = 0
                        if len(usuarios[inicial]) == 0:
                            print("-> AINDA NÃO FORAM CADASTRADAS NENHUM USUÁRIO <-")
                        else:
                            print("USUÁRIOS CADASTRADOS COM A LETRA '{}':".format(inicial))
                            for usuario in usuarios[inicial]:
                                cpf = usuario[0]
                                print("----------------------------------------------")
                                print("CPF: {0}{1}{2}.{3}{4}{5}.{6}{7}{8}-{9}{10}".format(cpf[0], cpf[1], cpf[2], cpf[3], cpf[4], cpf[5], cpf[6], cpf[7], cpf[8], cpf[9], cpf[10]))
                                print("NOME: {}".format(usuario[1]))
                                print("DATA DE NASCIMENTO: {}".format(usuario[2]))
                                print("OBRAS ALUGADAS: {}")
                                # for emprestimo in emprestimos:

                        print("DESEJA CONTINUAR VISUALIZANDO OS USUÁRIOS CADASTRADOS:")
                        continuarVisualizarUsuarios = verificar()

                elif (desejoUser == 2):
                    # Cadastrar Usuário:
                    print("------------ CADASTRAR USUÁRIO ------------")
                    continuarCadastrarUsuario = True
                    while (continuarCadastrarUsuario == True):
                        verificado = False
                        while (verificado == False):
                            try:
                                CPF = (int(input("DIGITE O CPF DO USUÁRIO (SEM TRAÇOS OU PONTOS):\n-> ")))
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
                                            verificado = True
                                else:
                                    print("O CPF É INVÁLIDO, POIS ELE DEVE CONTER EXATAMENTE 11 DIGITOS!!!")
                            except ValueError:
                                print("DIGITE APENAS NÚMEROS!!!")

                        existe = False
                        for inicial in usuarios:
                            for usuario in usuarios[inicial]:
                                if (usuario[0] == CPF):
                                    existe = True
                                    break
                            if (existe == True):
                                break

                        if (existe == True):
                            print("-> USUÁRIO JÁ CADASTRADO <-")
                        else:
                            verificado = False
                            while (verificado == False):
                                nomeUsuario = (input("DIGITE O NOME DO USUÁRIO:\n-> "))
                                nomeUsuario = nomeUsuario.strip()
                                nomeUsuario = nomeUsuario.title()
                                if (len(nomeUsuario) > 0):
                                    verificado = True
                                else:
                                    print("-> DESEJO INVÁLIDO <-")

                            verificado = False
                            while (verificado == False):
                                try:
                                    print("DIGITE A DATA DE NASCIMENTO DO USUÁRIO: ")
                                    diaNascimento = (int(input("DIGITE O DIA: ")))
                                    mesNascimento = (int(input("DIGITE O MÊS: ")))
                                    anoNascimento = (int(input("DIGITE O ANO: ")))

                                    if (anoNascimento > 0):
                                        if ((diaNascimento <= 30) and (mesNascimento == 4 or mesNascimento == 6 or mesNascimento == 9 or mesNascimento == 11)):
                                            verificado = True
                                        elif (diaNascimento <= 31) and (mesNascimento == 1 or mesNascimento == 3 or mesNascimento == 5 or mesNascimento == 7 or mesNascimento == 8 or mesNascimento == 10 or mesNascimento == 12):
                                            verificado = True
                                        elif ((diaNascimento <= 29) and (mesNascimento == 2)and (anoNascimento % 4 == 0)):
                                            verificado = True
                                        elif ((diaNascimento <= 28) and (mesNascimento == 2) and (anoNascimento % 4 != 0)):
                                            verificado = True
                                        else:
                                            print("-> DATA INVÁLIDA <-")
                                    else:
                                        print("-> DATA INVÁLIDA <-")
                                except ValueError:
                                    print("-> DIGITE APENAS NÚMEROS <-")

                            diaNascimento = str(diaNascimento)
                            if (len(diaNascimento) == 1):
                                diaNascimento = ("0" + diaNascimento)

                            mesNascimento = str(mesNascimento)
                            if (len(mesNascimento) == 1):
                                mesNascimento = ("0" + mesNascimento)

                            anoNascimento = str(anoNascimento)

                            dataNascimento = (diaNascimento + "/" + mesNascimento + "/" + anoNascimento)

                            inicialNomeUser = (nomeUsuario[0])

                            usuarios[inicialNomeUser].append((CPF, nomeUsuario, dataNascimento))

                        print("DESEJA CONTINUAR CADASTRANDO NOVOS USUÁRIOS:")
                        continuarCadastrarUsuario = verificar()

                elif (desejoUser == 3):
                    # Modificar usuário:
                    print("------------ MODIFICAR USUÁRIO ------------")
                    continuarModificarUsuarios = True
                    while (continuarModificarUsuarios == True):
                        verificado = False
                        while (verificado == False):
                            try:
                                cpfU = (int(input("DIGITE O CPF DO USUÁRIO (SEM TRAÇOS OU PONTOS):\n-> ")))
                                cpfU = str(cpfU)
                                if (len(cpfU) == 11):
                                    verificado = True
                                else:
                                    print("-> DESEJO INVÁLIDO <-")
                            except ValueError:
                                print("-> DIGITE APENAS NÚMEROS <-")

                        userCadastrado = False
                        for inicial in usuarios:
                            index = -1
                            for usuario in usuarios[inicial]:
                                index += 1
                                if (usuario[0] == cpfU):
                                    cpf = usuario[0]
                                    print("----------------------------------------------")
                                    print("CPF: {0}{1}{2}.{3}{4}{5}.{6}{7}{8}-{9}{10}".format(cpf[0], cpf[1], cpf[2], cpf[3], cpf[4], cpf[5], cpf[6], cpf[7], cpf[8], cpf[9], cpf[10]))
                                    print("NOME: {}".format(usuario[1]))
                                    print("DATA DE NASCIMENTO: {}".format(usuario[2]))
                                    userCadastrado = True
                                    break
                            if (userCadastrado == True):
                                break

                        if (userCadastrado == False):
                            print("-> USUÁRIO NÃO CADASTRADO <-")
                        else:
                            del usuarios[inicial][index]
                            verificado = False
                            while (verificado == False):
                                nomeUsuario = (input("DIGITE O NOME DO USUÁRIO:\n-> "))
                                nomeUsuario = nomeUsuario.strip()
                                nomeUsuario = nomeUsuario.title()
                                if (len(nomeUsuario) > 0):
                                    verificado = True
                                else:
                                    print("-> DESEJO INVÁLIDO <-")

                            verificado = False
                            while (verificado == False):
                                try:
                                    print("DIGITE A DATA DE NASCIMENTO DO USUÁRIO: ")
                                    diaNascimento = (int(input("DIGITE O DIA: ")))
                                    mesNascimento = (int(input("DIGITE O MÊS: ")))
                                    anoNascimento = (int(input("DIGITE O ANO: ")))

                                    if (anoNascimento > 0):
                                        if ((diaNascimento <= 30) and (mesNascimento == 4 or mesNascimento == 6 or mesNascimento == 9 or mesNascimento == 11)):
                                            verificado = True
                                        elif (diaNascimento <= 31) and (mesNascimento == 1 or mesNascimento == 3 or mesNascimento == 5 or mesNascimento == 7 or mesNascimento == 8 or mesNascimento == 10 or mesNascimento == 12):
                                            verificado = True
                                        elif ((diaNascimento <= 29) and (mesNascimento == 2)and (anoNascimento % 4 == 0)):
                                            verificado = True
                                        elif ((diaNascimento <= 28) and (mesNascimento == 2) and (anoNascimento % 4 != 0)):
                                            verificado = True
                                        else:
                                            print("-> DATA INVÁLIDA <-")
                                    else:
                                        print("-> DATA INVÁLIDA <-")
                                except ValueError:
                                    print("-> DIGITE APENAS NÚMEROS <-")

                            diaNascimento = str(diaNascimento)
                            if (len(diaNascimento) == 1):
                                diaNascimento = ("0" + diaNascimento)

                            mesNascimento = str(mesNascimento)
                            if (len(mesNascimento) == 1):
                                mesNascimento = ("0" + mesNascimento)

                            anoNascimento = str(anoNascimento)

                            dataNascimento = (diaNascimento + "/" + mesNascimento + "/" + anoNascimento)

                            inicialNomeUser = (nomeUsuario[0])

                            usuarios[inicialNomeUser].append((cpfU, nomeUsuario, dataNascimento))


                    print("DESEJA MODIFICAR OS DADOS DE MAIS ALGUM USÁRIO:")
                    continuarModificarUsuarios = verificar()
                                    
    
                elif (desejoUser == 4):
                    # Excluir usuário:
                    print("------------- EXCLUIR USUÁRIO -------------")
                    continuarExcluirUsuarios = True
                    while (continuarExcluirUsuarios == True):
                        verificado = False
                        while (verificado == False):
                            try:
                                cpfU = (int(input("DIGITE O CPF DO USUÁRIO (SEM TRAÇOS OU PONTOS):\n-> ")))
                                cpfU = str(cpfU)
                                if (len(cpfU) == 11):
                                    verificado = True
                                else:
                                    print("-> DESEJO INVÁLIDO <-")
                            except ValueError:
                                print("-> DIGITE APENAS NÚMEROS <-")

                        userCadastrado = False
                        for inicial in usuarios:
                            index = -1
                            for usuario in usuarios[inicial]:
                                index += 1
                                if (usuario[0] == cpfU):
                                    cpf = usuario[0]
                                    print("----------------------------------------------")
                                    print("CPF: {0}{1}{2}.{3}{4}{5}.{6}{7}{8}-{9}{10}".format(cpf[0], cpf[1], cpf[2], cpf[3], cpf[4], cpf[5], cpf[6], cpf[7], cpf[8], cpf[9], cpf[10]))
                                    print("NOME: {}".format(usuario[1]))
                                    print("DATA DE NASCIMENTO: {}".format(usuario[2]))
                                    userCadastrado = True

                                    print("REALMENTE DESEJA EXCLUIR O USUÁRIO:")
                                    desejoExcluir = verificar()
                                    if (desejoExcluir == 1):
                                        del usuarios[inicial][index]
                                        # RETIRAR OS EMPRÉSTIMOS CORRESPONDENTES TBM
                                
                        if (userCadastrado == False):
                            print("-> USUÁRIO NÃO CADASTRADO <-")

                        print("DESEJA EXCLUIR MAIS ALGUM USUÁRIO:")
                        continuarExcluirUsuarios = verificar()

                print("DESEJA CONTINUAR GERENCIANDO OS USUÁRIOS:")
                continuarGerenciarUsuarios = verificar()
                

        # Gereniar empréstimos:
        elif (desejo == 3):
            print("--------- GERENCIADOR DE EMPRÉSTIMOS ---------")
            continuarGerenciarEmprestimos = True
            while (continuarGerenciarEmprestimos == True):
                verificado = False
                while (verificado == False):
                    try:
                        desejoEmpres = (int(input("O QUE DESEJA:\n"\
                        "DIGITE:\n"\
                        "1- CADASTRAR EMPRÉSTIMO\n"\
                        "2- CADASTRAR DEVOLUÇÃO\n"\
                        "-> "
                        )))
                        if (1 <= desejo <= 2):
                            verificado = True
                        else:
                            print("-> DESEJO INVÁLIDO <-")
                    except ValueError:
                        print("-> DIGITE APENAS NÚMEROS! <-")

                if (desejoEmpres == 1):
                    # Cadastrar empréstimo da obra
                    print("Cadastrar empréstimo da obra")
                elif (desejoEmpres == 2):
                    # Cadastrar devolução da obra
                    print("Cadastrar devolução da obra")

                    
                continuarGerenciarEmprestimos = verificar()

        print("DESEJA CONTINUAR NO SISTEMA:")
        # Verifiar se o usuário deseja continuar no programa:   
        continuar_no_sistema = verificar()


    # Verifiar se o usuário deseja continuar no programa:
    else:    
        print("DESEJA CONTINUAR NO SISTEMA:")
        continuar_no_sistema = verificar()