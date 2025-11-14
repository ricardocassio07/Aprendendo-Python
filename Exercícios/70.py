# 70. Implemente um algoritmo de ordenação otimizado usando range:
numeros = []
continuarInserindo = True
while (continuarInserindo == True):
    try:
        num = (int(input("Digite um número: ")))
        numeros.append(num)
        desejoValido = False
        while (desejoValido == False):
            try:
                desejo = (int(input("Você deseja adicionar mais um número:\nDigite:\n1- Sim\n2- Não\n-> ")))
                if (1 <= desejo <= 2):
                    if (desejo == 1):
                        print("OK! VAMOS CONTINUAR ENTÃO...")
                        desejoValido = True
                    else:
                        print("OK! VAMOS PARA A PRÓXIMA ETAPA!!!")
                        desejoValido = True
                        continuarInserindo = False
                else:
                    print("DIGITE 1(SIM) OU 2(NÃO)!!!")
            except:
                print("DIGITE APENAS NÚMEROS!!!")
    except:
        print("DIGITE APENAS NÚMEROS!!!")
# Encontrar maior e menor número da lista:
for i in range(len(numeros)):
    parametro = numeros[i]
    if (i == 0):
        maior = parametro
        menor = parametro
    if (parametro < menor):
        menor = parametro
    if (parametro > maior):
        maior = parametro

# print(maior)
# print(menor)
# print()

# Após encontrarmos, vamos verificar de número em número se ele está presente na lista. Caso sim, vamos adicionar; caso não, vamos pular e verificar o próximo. E, assim, vamos ter a lista ordenada do menor para o maior:
numerosOrdenados = []
parametro = menor
while (parametro <= maior):
    for i in range(len(numeros)):
        if (parametro == numeros[i]):
            # print(parametro)
            # print(numeros[i])
            numerosOrdenados.append(parametro)
    parametro += 1

print(numerosOrdenados)