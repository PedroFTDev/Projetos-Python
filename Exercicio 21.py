'''
8) Escreva um programa que informe o valor de uma corrida de taxi. 
Para calcular o valor da corrida é necessário saber a distância percorrida em quilômetros
e qual o tipo da bandeira da corrida, 1 ou 2. 
Caso a bandeira seja 1, o preço do quilometro percorrido é  de R$ 1,80, se a bandeira for 2 o valor é de R$ 2,30.
Escreva um programa em linguagem python que solicite a distância percorrida em quilômetros e qual o tipo da bandeira da corrida e informe o valor da corrida
'''

# -*- coding: utf-8 -*-

print ("Valor da Corrida")

D1 = int(input("Distancia:"))
B1 = int(input("Bandeira:"))

if (B1 == 1): 
    Total = (D1 * 1.8)
    print ("O valor da corrida é:", Total, "R$")
    
if (B1 == 2): 
    Total2= D1 * 2.3
    print ("O valor da corrida é:", Total2, "R$")