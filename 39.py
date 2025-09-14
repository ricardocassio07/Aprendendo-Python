# 39. Crie um programa que simule um sistema de login.
usuario_cadastrado = "cassio"
senha_cadastrada = "1234"
usuario = input("Digite seu usuário: ")
senha = input("Digite sua senha: ")
if ((usuario == usuario_cadastrado) and (senha == senha_cadastrada)):
    print("LOGIN REALIZADO COM SUCESSO!!!\nSeja muito bem-vindo(a), {}!".format(usuario))
else:
    print("USUÁRIOS OU SENHA INCORRETOS!!!")