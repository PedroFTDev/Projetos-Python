'''
Faça um programa que peça para n pessoas a sua idade, ao final o programa
devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior
que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média
calculada.
'''

idade=0
somaIdades=0
qtdeIdades=0
médiaIdades=0

while(idade>=0):
    idade= float(input("Digite uma idade:"))
    if (idade>=0):
        somaIdades=somaIdades+idade
        qtdeIdades=qtdeIdades+1
print("A média é:", somaIdades/qtdeIdades)
médiaidades= somaIdades/qtdeIdades

if (médiaIdades<=25):
         print("A turma é jovem")
elif (médiaIdades>=26):
        print("A turma é adulta")
elif (médiaIdades>60):
        print("A turma é idosa")
