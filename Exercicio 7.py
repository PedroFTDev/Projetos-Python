'''
1) Escreva um programa para receber 3 valores inteiros do usuário e mostrar a sua média (que pode não ser inteira).
'''

# -*- coding: utf-8 -*-


print ("MEDIA DO ALUNO")

n1 = float(input("Digite a primeira nota:"))

n2 = float(input("Digite a segunda nota:"))

n3 = float(input("Digite a terceira nota:"))

Media = (n1 + n2 + n3) / 3

print ("A média do aluno é:",round (Media), "M")
