# 61. Desenvolva um analisador de texto que conte palavras, caracteres, frases e implemente busca avançada com expressões regulares.
import re
texto = (input("Digite um texto:\n-> "))
caracteres = (len(texto))

frases = (re.split(r"[.!?]+", texto))

# Retirando strings vazias da lista:
i = 0
while (i < len(frases)):
    # Quando removemos um item da lista, o próximo elemento ocupa sua posição e a largura da lista muda. Por isso, para garantir que todos os elementos sejam verificados, não aumentamos o 'i':
    if (frases[i] == ""):
        del frases[i]
    else:
        # Só avançamos (i += 1) quando nada foi removido, garantindo que todos os itens sejam verificados:
        i += 1

qtdFrases = (len(frases))

palavras = (re.split(r"[-,.!?()\s@#$%&*£¢]+", texto))

# Retirando strings vazias ou numéricas da lista:
i = 0
while (i < len(palavras)):
    # Quando removemos um item da lista, o próximo elemento ocupa sua posição e a largura da lista muda. Por isso, para garantir que todos os elementos sejam verificados, não aumentamos o 'i':
    if (palavras[i] == ""):
        del palavras[i]
    elif (palavras[i].isdigit()):
        del palavras[i]
    else:
        # Só avançamos (i += 1) quando nada foi removido, garantindo que todos os itens sejam verificados:
        i += 1

qtdPalavras = (len(palavras))

padrao = (input("Qual expressão deseja pesquisar?\n-> "))
padrao = (padrao.strip())
ocorrencias = (re.findall(padrao, texto))
qtdOcorrencias = (len(ocorrencias))

# TESTES:
# print(caracteres)
# print(frases)
# print(palavras)
# print(qtdPalavras)
# print(ocorrencias)

print("ANÁLISE DO TEXTO:")
print("O texto possui {} caracteres!".format(caracteres))
print("O texto possui {} frases!".format(qtdFrases))
print("O texto possui {} palavras!".format(qtdPalavras))
print("A expressão '{}' apareceu {} vezes no texto!".format(padrao, qtdOcorrencias))