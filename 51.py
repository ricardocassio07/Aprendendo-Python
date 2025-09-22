# 51. Crie um programa que valide um número de telefone brasileiro e formate-o corretamente usando try/except.
try:
    valido = False
    while (valido == False):
        ddd = (int(input("Digite o DDD do número: ")))
        telefone = (int(input("Digite o número de telefone: ")))
        ddd = str(ddd)
        telefone = str(telefone)
        if (len(ddd) == 2 and len(telefone) == 9):
            valido = True
        else:
            print("DIGITE UM NÚMERO VÁLIDO!!!")
    print("({}) {}{}{}{}{}-{}{}{}{}".format(ddd, telefone[0], telefone[1], telefone[2], telefone[3], telefone[4], telefone[5], telefone[6], telefone[7], telefone[8]))
    
except ValueError:
    print("Você deve digitar apenas números inteiros!")