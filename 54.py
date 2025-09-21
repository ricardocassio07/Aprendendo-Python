# 4. Crie um programa que analise uma lista de palavras e encontre anagramas usando manipulação de strings.
lista = ["roma", "banana", "macaco", "pera", "maça", "abacate", "perda", "mora", "amor", "ramo", "xícara", "alface", "tomate", "azul", "padre"]
anagramas = []
i = 0
# percorre cada palavra da lista
while (i < (len(lista))):
    palavra1 = lista[i]
    # lista com os caracteres da palavra que vamos utilizar como parâmetro para comparar com as letras das outras palavras:
    letras1 = sorted(palavra1)
    # agora vamos comparar com os outras palavras
    p = (i + 1)
    while (p < (len(lista))):
        palavra2 = lista[p]
        letras2 = sorted(palavra2)
        if letras1 == letras2:
            anagramas.append((palavra1, palavra2))
        p+=1
    i+=1
print("Anagramas encontrados:")
a=0
while (a < len(anagramas)):
    print(anagramas[a])
    a+=1