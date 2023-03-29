nota=0
somaNotas=0
qtdeNotas=0
while(nota>=0):
    nota= float(input("Digite uma nota:"))
    if (nota>=0):
        somaNotas=somaNotas+nota
        qtdeNotas=qtdeNotas+1
print("A média é:", somaNotas/qtdeNotas)