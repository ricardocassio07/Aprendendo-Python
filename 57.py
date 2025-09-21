# 7. Crie um programa que simule um jogo da velha com validação de jogadas e detecção de vitória.
import random
A1 = "a1"
A2 = "a2"
A3 = "a3"
B1 = "b1"
B2 = "b2"
B3 = "b3"
C1 = "c1"
C2 = "c2"
C3 = "c3"
jogoFinalizado = False
rodada = 1
jogadorDaVez = ""
while (jogoFinalizado == False):
    print("LINHAS - 'a', 'b' OU 'c'")
    print("COLUNAS - '1', '2' OU '3'")
    print("     1    2    3 ")
    print("a  | {} | {} | {} |".format(A1, A2, A3))
    print("b  | {} | {} | {} |".format(B1, B2, B3))
    print("c  | {} | {} | {} |".format(C1, C2, C3))

    if (rodada == 1):
        g = random.randint(0, 1)
        if (g == 0):
            jogadorDaVez = "❌"
        else:
            jogadorDaVez = "⭕"
    elif (rodada > 1):
        if (jogadorDaVez == "❌"):
            jogadorDaVez = "⭕"
        else:
            jogadorDaVez = "❌"
    print("JOGADOR DA VEZ: {}".format(jogadorDaVez))

    opçõesValidas = False
    while (opçõesValidas == False):
        try:
            l = (input("Em qual linha (A, B OU C) você deseja jogar?\n-> "))
            l = l.lower()
            c = (int(input("Em qual coluna (1, 2 OU 3) você deseja jogar?\n-> ")))
            if ((l == "a" or l == "b" or l == "c") and (1 <= c <= 3)):
                if (l == "a") and (c == 1):
                    if (A1 == "a1"):
                        A1 = jogadorDaVez
                        rodada += 1
                        opçõesValidas = True
                    else:
                        print("POSIÇÃO JÁ OCUPADA!!!")
                elif ((l == "a") and (c == 2)):
                    if (A2 == "a2"):
                        A2 = jogadorDaVez
                        rodada += 1
                        opçõesValidas = True
                    else:
                        print("POSIÇÃO JÁ OCUPADA!!!")
                elif ((l == "a") and (c == 3)):
                    if (A3 == "a3"):
                        A3 = jogadorDaVez
                        rodada += 1
                        opçõesValidas = True
                    else:
                        print("POSIÇÃO JÁ OCUPADA!!!")
                elif ((l == "b") and (c == 1)):
                    if (B1 == "b1"):
                        B1 = jogadorDaVez
                        rodada += 1
                        opçõesValidas = True
                    else:
                        print("POSIÇÃO JÁ OCUPADA!!!")
                elif ((l == "b") and (c == 2)):
                    if (B2 == "b2"):
                        B2 = jogadorDaVez
                        rodada += 1
                        opçõesValidas = True
                    else:
                        print("POSIÇÃO JÁ OCUPADA!!!")
                elif ((l == "b") and (c == 3)):
                    if (B3 == "b3"):
                        B3 = jogadorDaVez
                        rodada += 1
                        opçõesValidas = True
                    else:
                        print("POSIÇÃO JÁ OCUPADA!!!")
                elif ((l == "c") and (c == 1)):
                    if (C1 == "c1"):
                        C1 = jogadorDaVez
                        rodada += 1
                        opçõesValidas = True
                    else:
                        print("POSIÇÃO JÁ OCUPADA!!!")
                elif ((l == "c") and (c == 2)):
                    if (C2 == "c2"):
                        C2 = jogadorDaVez
                        rodada += 1
                        opçõesValidas = True
                    else:
                        print("POSIÇÃO JÁ OCUPADA!!!")
                elif ((l == "c") and (c == 3)):
                    if (C3 == "c3"):
                        C3 = jogadorDaVez
                        rodada += 1
                        opçõesValidas = True
                    else:
                        print("POSIÇÃO JÁ OCUPADA!!!")
            else:
                print("VOCÊ DEVE DIGITAR:\nLINHA = 'a', 'b', ou 'c'\nCOLUNAS = 1, 2 OU 3")
        except ValueError:
            print("DIGITE APENAS NÚMEROS!!!")
            
    if (A1 == A2 == A3):
        jogoFinalizado = True
    elif (B1 == B2 == B3):
        jogoFinalizado = True
    elif (C1 == C2 == C3):
        jogoFinalizado = True
    elif (A1 == B1 == C1):
        jogoFinalizado = True
    elif (A2 == B2 == C2):
        jogoFinalizado = True
    elif (A3 == B3 == C3):
        jogoFinalizado = True
    elif (A1 == B2 == C3):
        jogoFinalizado = True
    elif (A3 == B2 == C1):
        jogoFinalizado = True
    else:
        jogoFinalizado = False

    if (jogoFinalizado == True):
        print("Após {} rodadas, nós temos um vencedor!!!\nPARÁBENS, JOGADOR {}, VOCÊ FOI O GRANDE VENCEDOR DESSA PARTIDA!!!".format((rodada - 1), jogadorDaVez))
        print("     1    2    3 ")
        print("a  | {} | {} | {} |".format(A1, A2, A3))
        print("b  | {} | {} | {} |".format(B1, B2, B3))
        print("c  | {} | {} | {} |".format(C1, C2, C3))
        
    if (rodada == 10):
        print("IHHHH!!! DEU 'VELHA', PORTANTO, NÃO TEMOS VENCEDORES, O JOGO TERMINOU EMPATADO!!!")
        print("     1    2    3 ")
        print("a  | {} | {} | {} |".format(A1, A2, A3))
        print("b  | {} | {} | {} |".format(B1, B2, B3))
        print("c  | {} | {} | {} |".format(C1, C2, C3))