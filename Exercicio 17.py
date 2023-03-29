# -*- coding: utf-8 -*-

print("QUANTIDADE DE MOEDAS")

M1 = int(input("Digite a quantidade de Moedas de 1 centavo:"))

M2 = int(input("Digite a quantidade de Moedas de 5 centavos:"))

M3 = int(input("Digite a quantidade de Moedas de 10 centavos:"))

M4 = int(input("Digite a quantidade de Moedas de 25 centavos:"))

M5 = int(input("Digite a quantidade de Moedas de 50 centavos:"))

M6 = int(input("Digite a quantidade de Moedas de 1 real:"))

Total= (M1 + M2*5+ M3*10 + M4*25 + M5*50 + M6*100) / 100

print("A quantidade de moédas é:",Total , "R$")
