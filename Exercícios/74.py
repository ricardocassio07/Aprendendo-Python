'''
    74: Crie um sistema que analise dados de vendas de uma empresa, calculando
    estatísticas por período, vendedor e região. O sistema deve tratar dados inconsistentes e
    gerar relatórios detalhados.
Requisitos técnicos:
    - Use for com range para iterar por períodos
    - Implemente try-except para tratar dados inválidos
    - Use if-elif-else para categorização de desempenho
    - Crie função para cálculos estatísticos
    - Use while para menu interativo 
'''

# Local da loja | Valor total das vendas (NOS ÚLTIMOS 30 DIAS) | Quantidade de vendedores:
lojas = {
    "ZONA_LESTE":(12000, 3),
    "ZONA_OESTE":(6500, 3),
    "ZONA_SUL":(12500, 2),
    "ZONA_NORTE":(14600, 4)
}

# Nome do vendedor | Valor total vendido (NOS ÚLTIMOS 30 DIAS) | Sigla da loja (ZL: ZONA LESTE; Z0: ZONA OESTE; ZS: ZONA SUL; ZN: ZONA NORTE):
vendedores = {
    "carlos":(5000, "ZL"),
    "miguel":(3000, "ZL"),
    "josé":(4000, "ZL"),

    "henrique":(2600, "ZN"),
    "antônio":(3500, "ZN"),
    "lara":(2500, "ZN"),
    "maria":(6000, "ZN"),

    "martina":(4000, "ZO"),
    "ellen":(1500, "ZO"),
    "ana":(1000, "ZO"),

    "bruna":(6000, "ZS"),
    "matheus":(5000, "ZS"),
    "wagner":(1500, "ZS")
}

def sistema_de_gerenciamento():
    try:
        valido = False
        while (valido == False):
            desejo = (int(input(
                "O QUE DESEJA VISUALIZAR:\n"\
                "DIGITE:\n"\
                "1- ESTATÍSTICAS DE CADA LOJA\n"\
                "2- ESTATÍSTICAS DE CADA VENDEDOR\n"\
                "3- ESTATÍSTICAS POR PERÍODO\n"\
                "-> "
            )))
            if (1 <= desejo <= 3):
                valido = True
            else:
                print("-> DIGITE 1, 2 OU 3!!! <-")
        
        if (desejo == 1):
            for loja in lojas:
                print("-----------------------------------------------------------")
                print("REGIÃO: {}".format(loja))
                print("TOTAL VENDIDO: R${:.2f}".format(lojas[loja][0]))
                print("TOTAL DE VENDEDORES: {}".format(lojas[loja][1]))
        
        elif (desejo == 2):
            valido = False
            while (valido == False):
                opcaoRegiao = (int(input(
                    "DIGITE A REGIÃO DA LOJA EM QUE O VENDEDOR ATUA:\n"\
                    "DIGITE:\n"\
                    "1- ZL\n"\
                    "2- ZN\n"\
                    "3- ZO\n"\
                    "4- ZS\n"\
                    "-> "
                    )))

                if (1 <= opcaoRegiao <= 4):
                    valido = True
                else:
                    print("-> OPÇÃO INVÁLIDA!!! <-")
                
            if (opcaoRegiao == 1):
                regiao = "ZONA_LESTE"
                opcaoRegiao = "ZL"
            elif (opcaoRegiao == 2):
                regiao = "ZONA_NORTE"
                opcaoRegiao = "ZN"
            elif (opcaoRegiao == 3):
                regiao = "ZONA_OESTE"
                opcaoRegiao = "ZO"
            elif (opcaoRegiao == 4):
                regiao = "ZONA_SUL"
                opcaoRegiao = "ZS"
            
            print("OS VENDEDORES QUE TRABLHAM NA LOJA DA REGIÃO {} SÃO:".format(regiao))
            i = 0
            vendedoresRegiao = []
            for vendedor in vendedores:
                if (vendedores[vendedor][1] == opcaoRegiao):
                    i += 1
                    print("{}- {}".format(i, vendedor.upper()))
                    nome_do_vendedor = vendedor
                    vendedoresRegiao.append((nome_do_vendedor, i))
                    # print(i)
            
            # print(vendedoresRegiao)

            valido = False
            while (valido == False):
                opcaoVendedor = (int(input("SOBRE QUAL DESEJA OBTER MAIS INFORMAÇÕES?\nDIGITE O NÚMERO QUE VEM ANTES DE SEU NOME:\n-> ")))
                if (1 <= opcaoVendedor <= i):
                    valido = True
                    for x in range(len(vendedoresRegiao)):
                        if (vendedoresRegiao[x][1] == opcaoVendedor):
                            vendedor = vendedoresRegiao[x][0]
                            # print(vendedor)
                            print("\nAQUI ESTÃO AS ESTATÍSTICAS DO(A) {}:".format(vendedor.upper()))
                            print("TOTAL DE VENDAS: R${}".format(vendedores[vendedor][0]))
                            print("MÉDIA DE VENDAS DOS ÚLTIMOS 30 DIAS: R${:.2f}".format((vendedores[vendedor][0]) / 30))
                else:
                    print("-> OPÇÃO INVÁLIDA!!! <-")
        
        elif (desejo == 3):
            for loja in lojas:
                print("-----------------------------------------------------------")
                print("REGIÃO: {}".format(loja))
                print("MÉDIA DOS ÚLTIMOS 30 DIAS: R${:.2f}".format((lojas[loja][0]) / 30))        

    except ValueError:
        print("-> DIGITE APENAS NÚMEROS!!! <-")
            
        

print("------------- SEJA MUITO BEM-VINDO(A) -------------")
encerrar = False
while (encerrar == False):
    try:
        sistema_de_gerenciamento()
        valido = False
        while (valido == False):
            desejoContinuar = (int(input(
                "\nDESEJA CONTINUAR:\n"\
                "DIGITE:\n"\
                "1- SIM\n"\
                "2- NÃO\n"\
                "-> "
            )))
            if (1 <= desejoContinuar <= 2):
                valido = True
                if (desejoContinuar == 1):
                    print("VAMOS CONTINUAR ENTÃO...")
                else:
                    print("OK! FOI BOM TER VOCÊ CONOSCO!!!")
                    encerrar = True
            else:
                print("-> DIGITE 1 OU 2!!! <-")
        
    except ValueError:
        print("-> DIGITE APENAS NÚMEROS!!! <-")