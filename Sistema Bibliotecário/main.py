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
print()
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
            print("\n----------- GERENCIADOR DE OBRAS -----------")
            continuarGerenciarObra = True
            while (continuarGerenciarObra == True):
                verificado = False
                while (verificado == False):
                    try:
                        desejoObra = (int(input("O QUE DESEJA:\n"\
                        "DIGITE:\n"\
                        "1- VISUALIZAR OBRAS CADASTRADAS\n"\
                        "2- CADASTRAR OBRA\n"\
                        "3- MODIFICAR AS INFORMAÇÕES DE ALGUMA OBRA\n"\
                        "-> "
                        )))
                        if (1 <= desejoObra <= 3):
                            verificado = True
                        else:
                            print("-> DESEJO INVÁLIDO <-")
                    except ValueError:
                        print("-> DIGITE APENAS NÚMEROS! <-")
                
                
                if (desejoObra == 1):
                    # Mostrar obras catálogadas
                    print("Mostrar obras catálogadas")
                elif (desejoObra == 2):
                    # INSIRA O NOME, INSIRA O ANO, BLÁ BLÁ BLÁ
                    print("INSIRA O NOME, INSIRA O ANO, BLÁ BLÁ BLÁ")
                elif (desejoObra == 3):
                    # DIGITE O CÓDIGO DA OBRA QUE DESEJA MODIFICAR, DIGITE O NOME DA OBRA, DIGITE O ANO BLÁ BLÁ 
                    print("DIGITE O CÓDIGO DA OBRA QUE DESEJA MODIFICAR, DIGITE O NOME DA OBRA, DIGITE O ANO BLÁ BLÁ ")
                    
                verificado = False
                while (verificado == False):
                    try:
                        continuarGerenciarObras = (int(input("DESEJA CONTINUAR NA ABA DE GERENCIAMENTO DAS OBRAS:\n"\
                        "DIGITE:\n"\
                        "1- SIM\n"\
                        "2- NÃO\n"\
                        "-> "
                        )))
                        if (1 <= continuarGerenciarObras <= 2):
                            if (continuarGerenciarObras == 2):
                                verificado = True
                                continuarGerenciarObra = False
                        else:
                            print("-> DESEJO INVÁLIDO <-")
                    except ValueError:
                        print("-> DIGITE APENAS NÚMEROS! <-")
                

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
                    # Cadastrar empréstimo da obra
                    print("Cadastrar empréstimo da obra")
                elif (desejoObra == 2):
                    # Cadastrar devolução da obra
                    print("Cadastrar devolução da obra")
                    
                verificado = False
                while (verificado == False):
                    try:
                        continuarGerenciarUsuarios = (int(input("DESEJA CONTINUAR NA ABA DE GERENCIAMENTO DOS USUÁRIOS:\n"\
                        "DIGITE:\n"\
                        "1- SIM\n"\
                        "2- NÃO\n"\
                        "-> "
                        )))
                        if (1 <= continuarGerenciarUsuarios <= 2):
                            if (continuarGerenciarUsuarios == 2):
                                verificado = True
                                continuarGerenciarUsuarios = False
                        else:
                            print("-> DESEJO INVÁLIDO <-")
                    except ValueError:
                        print("-> DIGITE APENAS NÚMEROS! <-")
                

        # Gereniar empréstimos:
        elif (desejo == 3):
            print("\n--------- GERENCIADOR DE EMPRÈSTIMOS ---------")
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
                    # Mostrar usuários cadastrados
                    print("Mostrar usuários cadastrados")
                elif (desejoObra == 2):
                    # Cadastrar usuário, pedir nome, cpf, blá blá
                    print("Cadastrar usuário, pedir nome, cpf, blá blá")
                elif (desejoObra == 3):
                    # Digite o cpf do usuário, modificar nome, modificar email, modificar data de nascimento
                    print("Digite o cpf do usuário, modificar nome, modificar email, modificar data de nascimento")
                    
                verificado = False
                while (verificado == False):
                    try:
                        continuarGerenciarEmprestimo = (int(input("DESEJA CONTINUAR NA ABA DE GERENCIAMENTO DOS EMPRÉSTIMOS:\n"\
                        "DIGITE:\n"\
                        "1- SIM\n"\
                        "2- NÃO\n"\
                        "-> "
                        )))
                        if (1 <= continuarGerenciarEmprestimo <= 2):
                            if (continuarGerenciarEmprestimo == 2):
                                verificado = True
                                continuarGerenciarUsuarios = False
                        else:
                            print("-> DESEJO INVÁLIDO <-")
                    except ValueError:
                        print("-> DIGITE APENAS NÚMEROS! <-")


        verificado = False
        while (verificado == False):
            try:
                desejoContinuar = (int(input("DESEJA CONTINUAR NO SISTEMA:\n"\
                "DIGITE:\n"\
                "1- SIM\n"\
                "2- NÃO\n"\
                "-> "
                )))
                if (1 <= desejoContinuar <= 2):
                    verificado = True
                    if (desejoContinuar == 2):
                        print("OK! FOI BOM TER VOCÊ CONOSCO!!! (^_^)")
                        continuar_no_sistema = False
                else:
                    print("-> DESEJO INVÁLIDO <-")
            except ValueError:
                print("-> DIGITE APENAS NÚMEROS! <-")



    # Encerrar programa:
    else:    
        verificado = False
        while (verificado == False):
            try:
                desejoContinuar = (int(input("DESEJA CONTINUAR NO SISTEMA:\n"\
                "DIGITE:\n"\
                "1- SIM\n"\
                "2- NÃO\n"\
                "-> "
                )))
                if (1 <= desejoContinuar <= 2):
                    verificado = True
                    if (desejoContinuar == 2):
                        print("OK! FOI BOM TER VOCÊ CONOSCO!!! (^_^)")
                        continuar_no_sistema = False
                else:
                    print("-> DESEJO INVÁLIDO <-")
            except ValueError:
                print("-> DIGITE APENAS NÚMEROS! <-")