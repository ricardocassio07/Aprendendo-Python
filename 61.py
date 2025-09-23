# 61. Desenvolva um analisador de texto que conte palavras, caracteres, frases e implemente busca avançada com expressões regulares.
import re
texto = (input("Digite um texto:\n-> "))
caracteres = (len(texto))

palavras = re.split(r"[-,.!?()\s@#$%&*£¢]+", texto)

i = 0
while (i < len(palavras)):
    if (palavras[i] == ""):
        del palavras[i]
    else:
        i += 1

qtdPalavras = len(palavras)

print(caracteres)
print(palavras)
print(qtdPalavras)
# print(palavras)
# print(frases)
