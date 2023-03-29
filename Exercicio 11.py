# -*- coding: utf-8 -*-

print ("SALARIO")

H1 = float(input("Digite a quantidade de horas normais:"))

H2 = float(input("Digite a quantidade de horas extras:"))

SalarioBruto = H1*10 + H2*15

SalarioLiquido = SalarioBruto *0.9

print ("Salario Bruto do funcionario é:", SalarioBruto, "R$")
print ("Salario Liquido do funcionario é:", SalarioLiquido, "R$")
