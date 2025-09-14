# 38. Escreva um programa que verifique se um caractere é vogal ou consoante
c = (input("Digite um caractere: "))
if ((c == "a") or (c == "A") or (c == "e") or (c == "E") or (c == "i") or (c == "I") or (c == "o") or (c == "O") or (c == "u") or (c == "U")):
    print("A caractere '{}' é uma vogal!".format(c))
else:
    print("A caractere '{}' não é uma vogal!".format(c))