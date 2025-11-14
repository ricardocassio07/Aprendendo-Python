# 66. Crie um sistema de indexação reversa para processar dados em diferentes direções.
frases = {}
indice_reverso = {}
index = 0
continuar = True
while (continuar == True):
    index += 1
    frase = (input("DIGITE A {0}º FRASE: ".format(index)))
    frases[index] = frase
    # Separando as palavras da frase:
    palavras = frase.split()

    # Adicionando as ocorreências da palavra nas frases inseridas:
    for palavra in palavras:
        # Todos os caracteres minúsculos:
        palavra = palavra.lower()
        # Caso as palavras não sejam letras isoladas ou preposições:
        if palavra not in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "ante", "após", "até", "com", "contra", "de", "desde", "em", "entre", "para", "perante", "por", "sem", "sob", "sobre", "trás"]:
            # Caso ela ainda não esteja na lista... ADICIONA:
            if palavra not in indice_reverso:
                indice_reverso[palavra] = set()
            # Depois vamos adicionar o indice da frase que ela aparece:
            indice_reverso[palavra].add(index)

    valido = False
    while (valido == False):
        try:
            desejo = (int(input("Você deseja adicionar mais alguma frase?\nDigite:\n1- Sim\n2- Não\n-> ")))
            if (1<=desejo<=2):
                valido = True
                if (desejo == 1):
                    print("Ok! Vamos continnuar!!!")
                else:
                    print("Ok! Vamos para a próxima etapa!!!")
                    continuar = False
            else:
                print("Você deve digitar 1 ou 2!!!")
        except:
            print("Você deve digitar apenas números inteiros!!!")

# Mostra o índice reverso
print("\nÍndice reverso:")
# Trasnformando os elementos do dicionário em tupla:
for palavra, frase in indice_reverso.items():
    print(f"{palavra}: {sorted(frase)}")