# 49. Crie um programa que calcule o salário líquido com base no salário bruto.
salarioBruto = (float(input("Digite o valor do seu salário bruto: R$")))
inss = (salarioBruto * 0.11)
outros = (salarioBruto * 0.15)
salarioLiquido = (salarioBruto - (inss + outros))
print("Com desconto do INSS (11%) e de outros impostos (15%), o seu salário liquído será igual a R${:.2f}! ".format(salarioLiquido))