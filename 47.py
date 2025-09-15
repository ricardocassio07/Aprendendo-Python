# 47. Crie um programa que simule um jogo de adivinhação.
print("Pense em um número de 1 a 50 e eu vou tentar adivinhar!!!")
nMenor = 1
nMaior = 50
parar = False
while (parar == False): 
    if (nMenor > nMaior):
        print("PARECE QUE VOCÊ DIGITOU RESPOSTAS INCOERENTES!!!")
        parar = True
    palpite = ((nMenor + nMaior) // 2)
    resposta = (int(input("Você pensou no número {}?\nDIGITE:\n1. Sim, pensei no número {}!\n2. Não, pensei em um número MAIOR que {}!\n3. Não, pensei em um número MENOR que {}!\n-> ".format(palpite, palpite, palpite, palpite))))
    if (resposta == 1):
        print("HUUUUHHUUULLL! EU CONSEGUI!!! 😎🥳🎉")
        parar = True
    elif (resposta == 2):
        nMenor = (palpite + 1)
    elif (resposta == 3):
        nMaior = (palpite - 1)
    else:
        print("VOCÊ DEVE DIGITAR APENAS OS NÚMEROS: 1, 2 OU 3!!!")