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
import json
from ferramentas import (
    verificar_ou_criar_json,
    carregar_json,
    salvar_json,
    converter_listas_para_tuplas,
    converter_tuplas_para_listas
)

letras = [
    "A","B","C","D","E","F","G","H","I","J","K","L","M",
    "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
]

arquivoDadosObras = "dadosObras.json"
arquivoDadosUsuarios = "dadosUsuarios.json"
arquivoDadosEmprestimos = "emprestimos.json"

estrutura_obras = {
    "A": [], "B": [], "C": [], "D": [], "E": [], "F": [], "G": [], "H": [],
    "I": [], "J": [], "K": [], "L": [], "M": [], "N": [], "O": [], "P": [],
    "Q": [], "R": [], "S": [], "T": [], "U": [], "V": [], "W": [], "X": [],
    "Y": [], "Z": [], "NUM": []
}

estrutura_usuarios = {
    "A": [], "B": [], "C": [], "D": [], "E": [], "F": [], "G": [], "H": [],
    "I": [], "J": [], "K": [], "L": [], "M": [], "N": [], "O": [], "P": [],
    "Q": [], "R": [], "S": [], "T": [], "U": [], "V": [], "W": [], "X": [],
    "Y": [], "Z": []
}

estrutura_emprestimos = []

# Verificar os arquivos:
verificar_ou_criar_json(arquivoDadosObras, estrutura_obras)
verificar_ou_criar_json(arquivoDadosUsuarios, estrutura_usuarios)
verificar_ou_criar_json(arquivoDadosEmprestimos, estrutura_emprestimos)

# Carregar dados convertendo listas → tuplas
obras = carregar_json(arquivoDadosObras)
usuarios = carregar_json(arquivoDadosUsuarios)
emprestimos = carregar_json(arquivoDadosEmprestimos)

salvar_json(arquivoDadosObras, converter_tuplas_para_listas(obras))
salvar_json(arquivoDadosUsuarios, converter_tuplas_para_listas(usuarios))
salvar_json(arquivoDadosEmprestimos, emprestimos)


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
                                if (1 <= opcao <= 6):
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
                                    # print(obra)
                                    print("----------------------------------------------")
                                    print("NOME: {}".format(obra['titulo']))
                                    print("AUTOR: {}".format(obra['autor']))
                                    print("ANO: {}".format(obra['ano']))
                                    print("GÊNERO: {}".format(obra['genero']))
                                    print("DISPONIBILIDADE PARA EMPRÉSTIMO: {}".format(obra['status']))

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

                            qtdeObras = 0
                            for inicial in obras:
                                for obra in obras[inicial]:
                                    if (obra['autor'] == autor):
                                        print("----------------------------------------------")
                                        print("NOME: {}".format(obra['título']))
                                        print("ANO: {}".format(obra['ano']))
                                        print("GÊNERO: {}".format(obra['genero']))
                                        print("DISPONIBILIDADE PARA EMPRÉSTIMO: {}".format(obra['status']))
                                        qtdeObras += 1

                            if (qtdeObras == 0):
                                print("-> AINDA NÃO FORAM CADASTRADAS NENHUMA OBRA <-")

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

                            qtdeObras = 0
                            for inicial in obras:
                                for obra in obras[inicial]:
                                    if (obra['ano'] == ano):
                                        print("----------------------------------------------")
                                        print("NOME: {}".format(obra['titulo']))
                                        print("AUTOR: {}".format(obra['autor']))
                                        print("GÊNERO: {}".format(obra['genero']))
                                        print("DISPONIBILIDADE PARA EMPRÉSTIMO: {}".format(obra['status']))

                            if (qtdeObras == 0):
                                print("-> AINDA NÃO FORAM CADASTRADAS NENHUMA OBRA <-")

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

                            qtdeObras = 0
                            for inicial in obras:
                                for obra in obras[inicial]:
                                    if (obra['genero'] == genero):
                                        print("----------------------------------------------")
                                        print("NOME: {}".format(obra['nome']))
                                        print("AUTOR: {}".format(obra['autor']))
                                        print("ANO: {}".format(obra['ano']))
                                        print("DISPONIBILIDADE PARA EMPRÉSTIMO: {}".format(obra['status']))
                                        
                            if (qtdeObras == 0):
                                print("-> AINDA NÃO FORAM CADASTRADAS NENHUMA OBRA <-")

                        # 5- LIVROS INICIADOS COM NÚMERO
                        elif (opcao == 5):
                            if len(obras["NUM"]) == 0:
                                print("-> AINDA NÃO FORAM CADASTRADAS NENHUMA OBRA <-")
                            else:
                                for obra in obras["NUM"]:
                                    print("----------------------------------------------")
                                    print("NOME: {}".format(obra['titulo']))
                                    print("AUTOR: {}".format(obra['autor']))
                                    print("ANO: {}".format(obra['ano']))
                                    print("GÊNERO: {}".format(obra['genero']))
                                    print("DISPONIBILIDADE PARA EMPRÉSTIMO: {}".format(obra['status']))


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

                            obraEncontrada = False
                            if (len(obras[(nomeObra[0].upper())]) == 0):
                                print("-> AINDA NÃO FORAM CADASTRADAS NENHUMA OBRA <-")
                            else:
                                for inicial in obras:
                                    for obra in obras[inicial]:
                                        if (((obra['titulo']).lower()) == nomeObra):
                                            print("----------------------------------------------")
                                            print("NOME: {}".format(obra['titulo']))
                                            print("AUTOR: {}".format(obra['autor']))
                                            print("ANO: {}".format(obra['autor']))
                                            print("GÊNERO: {}".format(obra['genero']))
                                            print("DISPONIBILIDADE PARA EMPRÉSTIMO: {}".format(obra['status']))
                                            obraEncontrada = True
                                            break
                                    if (obraEncontrada == True):
                                        break
                            
                            if (obraEncontrada == False):
                                print("-> OBRA AINDA NÃO CATÁLOGADA <-")

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

                        obra = {
                            "titulo": nomeObra,
                            "autor": nomeAutor,
                            "ano": ano,
                            "genero": genero,
                            "status": "DISPONÍVEL"
                            }
                        # print(obra)
                        # print(obra[0])
                        primeiraLetra = (nomeObra[0].upper())
                        if (primeiraLetra in obras):
                            # print(primeiraLetra, type(obras[primeiraLetra]), type(obra))
                            obras[primeiraLetra].append(obra)
                            salvar_json(arquivoDadosObras, obras)
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
                                    codigoObra = (int(input("DIGITE O CÓDIGO DA OBRA QUE DESEJA MODIFICAR:\n-> ")))
                                
                                    if (1 <= codigoObra <= codigo):
                                        verificado = True
                                    else:
                                        print("-> DESEJO INVÁLIDO <-")
                                except ValueError:
                                    print("-> DIGITE APENAS NÚMEROS <-")


                        verificado = False
                        while (verificado == False):
                            try:
                                print("----------------------------------------------")
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
                        "4- EXCLUIR USUÁRIO\n"
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
                                    break
                            if (userCadastrado == True):
                                break
                                
                        if (userCadastrado == False):
                            print("-> USUÁRIO NÃO CADASTRADO <-")
                        else:
                            print("REALMENTE DESEJA EXCLUIR O USUÁRIO:")
                            desejoExcluir = verificar()
                            if (desejoExcluir == 1):
                                del usuarios[inicial][index]
                                # RETIRAR OS EMPRÉSTIMOS CORRESPONDENTES TBM

                        print("DESEJA EXCLUIR MAIS ALGUM USUÁRIO:")
                        continuarExcluirUsuarios = verificar()

                print("DESEJA CONTINUAR GERENCIANDO OS USUÁRIOS:")
                continuarGerenciarUsuarios = verificar()
                

        # Gerenciar empréstimos:
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
                    print("------------ CADASTRAR EMPRÉSTIMO ------------")
                    continuarCadastrandoEmprestimo = True
                    while (continuarCadastrandoEmprestimo == True):
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
                            
                            verificado = False
                            while (verificado == False):
                                letra = (input("DIGITE A LETRA:\n-> "))
                                # Ajustando a letra para minúsculo:
                                letra = letra.upper()
                                if (letra in letras):
                                    verificado = True
                                else:
                                    print("-> DESEJO INVÁLIDO <-")
                            
                            codigo = 0
                            if len(obras[letra]) == 0:
                                print("-> AINDA NÃO FORAM CADASTRADAS NENHUMA OBRA <-")
                            else:
                                for obra in obras[letra]:
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
                                        codigoObra = (int(input("DIGITE O CÓDIGO DA OBRA QUE O USUÁRIO DESEJA ALUGAR:\n-> ")))
                                    
                                        if (1 <= codigoObra <= codigo):
                                            verificado = True
                                        else:
                                            print("-> DESEJO INVÁLIDO <-")
                                    except ValueError:
                                        print("-> DIGITE APENAS NÚMEROS <-")

                                if (obras[letra][(codigoObra - 1)][4] == ("DISPONÍVEL")):
                                    print("-> OBRA DISPONÍVEL PARA EMPRÉSTIMO <-")
                                    nomeObra = obras[letra][(codigoObra - 1)][0]
                                    nomeAutor = obras[letra][(codigoObra - 1)][1]
                                    ano = obras[letra][(codigoObra - 1)][2]
                                    genero = obras[letra][(codigoObra - 1)][3]
                                    del obras[letra][(codigoObra - 1)]
                                    obras[letra].append((nomeObra, nomeAutor, ano, genero, "INDISPONÍVEL"))
                                    emprestimos.append((cpfU, obras[letra][(codigoObra - 1)][0]))
                                else:
                                    print("-> OBRA INDISPONÍVEL PARA EMPRÉSTIMO <-")


                        print("DESEJA CADASTRAR MAIS ALGUM EMPRÉSTIMO:")
                        continuarCadastrandoEmprestimo = verificar()
                        
                elif (desejoEmpres == 2):
                    # Cadastrar devolução da obra
                    print("------------ CADASTRAR DEVOLUÇÃO ------------")
                    continuarCadastrandoDevolucao = True
                    while (continuarCadastrandoDevolucao == True):
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


                        codigo = 0
                        usuerRealizouEmprestimo = False
                        for emprestimo in emprestimos:
                            if (emprestimo[0] == cpfU):
                                print("---------------------------------------------")
                                usuerRealizouEmprestimo = True
                                codigo += 1
                                print("CÓDIGO: {}".format(codigo))
                                print("OBRA: {}".format(emprestimo[1]))

                        if (usuerRealizouEmprestimo == False):
                            print("-> O USUÁRIO NÃO ALUGOU NENHUM LIVRO <-")
                        else:
                            continnuarComEsseUsuario = True
                            while (continnuarComEsseUsuario == True):
                                verificado = False
                                while (verificado == False):
                                    try:
                                        codigoObra = (int(input("DIGITE O CÓDIGO DO EMPRÉSTIMO A SER EXCLUIDO:\n-> ")))
                                        if (1 <= codigoObra <= codigo):
                                            verificado = True
                                        else:
                                            print("-> DESEJO INVÁLIDO <-")
                                    except ValueError:
                                        print("-> DIGITE APENAS NÚMEROS <-")
                                
                                nObra = emprestimos[(codigoObra - 1)][1]
                                print(nObra)
                                del emprestimos[(codigoObra - 1)]

                                for inicial in obras:
                                    index = -1
                                    for obra in obras[inicial]:
                                        index += 1
                                        if (obra[0] == nObra):
                                            nomeObra = obra[0]
                                            nomeAutor = obra[1]
                                            ano = obra[2]
                                            genero = obra[3]
                                            del obras[inicial][index]
                                            obras[inicial].append((nomeObra, nomeAutor, ano, genero, "DISPONÍVEL"))
                                
                                print("DESEJA CADASTRAR OUTRA DEVOLUÇÃO DESSE USUÁRIO")
                                continnuarComEsseUsuario = verificar()
                                        
                        print("DESEJA CADASTRAR OUTRA DEVOLUÇÃO:")
                        continuarCadastrandoDevolucao = verificar()
                
                print("DESEJA CONTINUAR GERENCIANDO OS EMPRÉSTIMOS DOS USUÁRIOS:")
                continuarGerenciarEmprestimos = verificar()

        print("DESEJA CONTINUAR NO SISTEMA:")
        # Verifiar se o usuário deseja continuar no programa:   
        continuar_no_sistema = verificar()


    # Verifiar se o usuário deseja continuar no programa:
    else:    
        print("DESEJA CONTINUAR NO SISTEMA:")
        continuar_no_sistema = verificar()