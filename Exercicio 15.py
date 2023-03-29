'''
4) Dado que a fórmula para conversão de Fahrenheit para Celsius é C = 5/9 (F – 32), 
faça um programa que leia um valor de temperatura em Fahrenheit e exiba em Celsius.
'''

# -*- coding: utf-8 -*-


print ("TEMPERATURA DO AMBIENTE")

F = int(input("Digite a temperatura do ambiente"))

Temp= 5/9 * (F-32)


print ("A TEMPERATURA DO AMBIENTE É:", Temp, "°C")