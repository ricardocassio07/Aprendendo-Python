# 3. Desenvolva um sistema de paginação usando range para dividir listas grandes.

lista = []
for i in range(1, 51):
    if (i < 10):
        lista.append("{0} ................................".format(i))
    else:
        lista.append("{0} ...............................".format(i))

def mostrar():
    continuar = True
    while (continuar == True):
        try:
            pagina = int(input("Qual página deseja visualizar?\n-> Página: "))
            qtdPaginas = ((len(lista)) / 10)
            if (1<=pagina<=qtdPaginas):
                pagina -= 1
                pagina *= 10
                for i in range(pagina, (pagina + 10)):
                    print(lista[i])
                valido = False
                while (valido == False):
                    try:
                        desejo = (int(input("Deseja continuar?\nDigite:\n1- Sim\n2- Não\n-> ")))
                        if (1<=desejo<=2):
                            if (desejo == 1):
                                print("Ok! Vamos contnuar então!!!")
                                valido = True
                            else:
                                print("Ok! Foi ótimo ter você conosco!!!")
                                valido = True
                                continuar = False
                        else:
                            print("Você deve digitar 1 ou 2!!!")
                    except:
                        print("Você deve digitar apenas números inteiros!!!")
            else:
                print("O livro possui apenas {0} páginas!!!".format((len(lista))/10))
        except ValueError:
            print("Você deve digitar apenas números inteiros!!!")

mostrar()