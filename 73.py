'''
    73: Desenvolva um sistema de autenticação que permita ao usuário fazer login com
    tentativas limitadas. O sistema deve ter diferentes níveis de usuário e implementar
    bloqueio temporário após falhas consecutivas.
Requisitos técnicos:
    - Use while para controlar o loop de tentativas
    - Implemente try-except para tratamento de entrada
    - Use if-elif-else para diferentes níveis de acesso
    - Use range para controlar tempo de bloqueio
    - Crie função para validação de credenciais
'''
import time
# Criação dos usuários e das senhas:
usuarios = {
    "carlos":(78809, "gerente"),
    "maria":(90876, "vendedor"),
    "josé":(90789, "vendedor"),
    "pedro":(35671, "auxiliar"),
    "enrique":(81792, "auxiliar")
}

# Função para verifcar credenciais:
def verificarCargo(usuario, lista = usuarios):
    global tentativas
    verificado = False
    while (verificado == False):
        try:
            cargo = (int(input("Qual o seu ccargo?\nDigite:\n1- Gerente\n2- Vendedor\n3- Auxilizar\n-> ")))
            if (1 <= cargo <= 3):
                verificado = True
                if (cargo == 1):
                    opcao = "gerente"
                elif (cargo == 2):
                    opcao = "vendedor"
                elif (cargo == 3):
                    opcao = "auxiliar"
                if (usuarios[usuario][1] == opcao):
                    print("OPÇÃO VÁLIDA!!!")
                    print("SEJA MUITO BEM-VINDO(A), {}!".format(usuario))
                    tentativas = 6
                else:
                    print("OPÇÃO INVÁLIDA!!!")
                    segundos = 0
                    for i in range(1, 6):
                        time.sleep(1)
                        if (i == 1):
                            print("ESPERE...")
                        h = "00"
                        m = "00"
                        segundos += 1
                        segundo = ("0{}".format(segundos))
                        print("{0}:{1}:{2}".format(h, m, segundo))
            else:
                print("DIGITE 1, 2 OU 3!!!")
        except ValueError:
            print("DIGITE APENAS NÚMEROS!!!")

# Inserção:
num_de_tentativas = 5
tentativas = 1
while (tentativas <= num_de_tentativas):
    u = (input("Digite o usuário:\n-> "))
    u = u.strip()
    while True:
        try:
            s = (input("Digite a senha:\n-> "))
            s = s.strip()
            if (len(s) != 5):
                    print("A SENHA POSSUI 5 DÍGITOS!!!")
            else:
                s = int(s)
                break
        except ValueError:
            print("A SENHA É TOTALMENTE NÚMERICA!!!")
    if (u in usuarios and (usuarios[u][0] == s)):
        print("USUÁRIO E SENHA VÁLIDOS!!!")
        verificarCargo(u)
    else:
        if(tentativas == 5):
            print("SUAS TENTATIVAS ACABARAM! POR FAVOR, INICIE O PROGRAMA NOVAMENTE!")
        else:
            print("USUÁRIO OU SENHA INVÁLIDO!!!")
            segundos = 0
            for i in range(1, 6):
                time.sleep(1)
                if (i == 1):
                    print("ESPERE...")
                h = "00"
                m = "00"
                segundos += 1
                segundo = ("0{}".format(segundos))
                print("{0}:{1}:{2}".format(h, m, segundo))
    tentativas += 1