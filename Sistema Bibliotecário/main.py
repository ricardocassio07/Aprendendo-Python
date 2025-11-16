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
usuario = {
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


def verificarPermanencia():             
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
                if (continuarNaSecao == 2):
                    verificado = True
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
                        if (1 <= desejoObra <= 4):
                            verificado = True
                        else:
                            print("-> DESEJO INVÁLIDO <-")
                    except ValueError:
                        print("-> DIGITE APENAS NÚMEROS! <-")
                
                
                if (desejoObra == 1):
                    # Mostrar obras catálogadas
                    print("--------------- MOSTRAR OBRA ---------------")
                    pararDeMostrarObras = False
                    while (pararDeMostrarObras == False):
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
                        pararDeMostrarObras = verificarPermanencia()



                        
                elif (desejoObra == 2):
                    # INSERIR OBRA
                    print("--------------- INSERIR OBRA ---------------")
                    pararDeInserirObras = False
                    while (pararDeInserirObras == False):
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


                        obra = (nomeObra, nomeAutor, ano, "DISPONÍVEL")
                        # print(obra)
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
                        pararDeInserirObras = verificarPermanencia()
                    
                elif (desejoObra == 3):
                    # MODIFICAR OBRA
                    print("-------------- MODIFICAR OBRA --------------")
                    pararDeModificarObras = False
                    while (pararDeModificarObras == False):
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
                        pararDeModificarObras = verificarPermanencia()

                elif (desejoObra == 4):
                    # EXCLUIR OBRA
                    print("--------------- EXCLUIR OBRA ---------------")
                    pararDeModificarObras = False
                    while (pararDeModificarObras == False):
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
                        pararDeModificarObras = verificarPermanencia()
                    
                continuarGerenciarObras = verificarPermanencia()
                

        # Gerenciar usuários:
        elif (desejo == 2):
            print("\n---------- GERENCIADOR DE USUÁRIOS ----------")
            continuarGerenciarUsuarios = True
            while (continuarGerenciarUsuarios == True):
                verificado = False
                while (verificado == False):
                    try:
                        desejoObra = (int(input("O QUE DESEJA:\n"\
                        "DIGITE:\n"\
                        "1- VISUALIZAR USUÁRIOS CADASTRADAS\n"\
                        "2- CADASTRAR USUÁRIO\n"\
                        "3- MODIFICAR AS INFORMAÇÕES DE ALGUM USUÁRIO\n"
                        "-> "
                        )))
                        if (1 <= desejoObra <= 3):
                            verificado = True
                        else:
                            print("-> DESEJO INVÁLIDO <-")
                    except ValueError:
                        print("-> DIGITE APENAS NÚMEROS! <-")

                    
                if (desejoObra == 1):
                    # Mostrar usuários cadastrados
                    print("Mostrar usuários cadastrados")
                elif (desejoObra == 2):
                    # Cadastrar usuário, pedir nome, cpf, blá blá
                    print("Cadastrar usuário, pedir nome, cpf, blá blá")
                elif (desejoObra == 3):
                    # Digite o cpf do usuário, modificar nome, modificar email, modificar data de nascimento
                    print("Digite o cpf do usuário, modificar nome, modificar email, modificar data de nascimento")
    
                continuarGerenciarUsuarios = verificarPermanencia()
                

        # Gereniar empréstimos:
        elif (desejo == 3):
            print("\n--------- GERENCIADOR DE EMPRÉSTIMOS ---------")
            continuarGerenciarEmprestimos = True
            while (continuarGerenciarEmprestimos == True):
                verificado = False
                while (verificado == False):
                    try:
                        desejo = (int(input("O QUE DESEJA:\n"\
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

                if (desejoObra == 1):
                    # Cadastrar empréstimo da obra
                    print("Cadastrar empréstimo da obra")
                elif (desejoObra == 2):
                    # Cadastrar devolução da obra
                    print("Cadastrar devolução da obra")

                    
                continuarGerenciarEmprestimos = verificarPermanencia()

        print("DESEJA CONTINUAR NO SISTEMA:")
        # Verifiar se o usuário deseja continuar no programa:   
        continuar_no_sistema = verificarPermanencia()


    # Verifiar se o usuário deseja continuar no programa:
    else:    
        print("DESEJA CONTINUAR NO SISTEMA:")
        continuar_no_sistema = verificarPermanencia()