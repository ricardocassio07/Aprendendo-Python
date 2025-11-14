# 30. Escreva um programa que classifique a nota de um aluno.
n = (float(input("Digite a nota do aluno: ")))
if (n >= 6):
    print("O aluno obteve nota {}, portanto, não precisará fazer recuperação!".format(n))
elif (n == 5):
    print("O aluno obteve nota 5, portanto, terá que fazer recuperação!")
else:
    print("O aluno obteve nota {}, portanto, não poderá fazer recuperção!".format(n))