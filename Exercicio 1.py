# -*- coding: utf-8 -*-


print ("QUANTIDADE DE MATERIAL")
nome = input("Digite o seu nome:")

qtdeP = int(input("Digite a quantidade de camisetas P: "))

qtdeM = int(input("Digite a quantidade de camisetas M: "))

qtdeG = int(input("Digite a quantidade de camisetas G: "))

Total= qtdeP*10 + qtdeM*12 + qtdeG*15

print ("o total da compra do cliente:", nome, "é: R$", Total)

