notaProva=float(input("Digite a nota da sua prova (0-10): "))

while(notaProva<0 or notaProva>10):
    print("Nota Invalida")
    notaProva=float(input("Digite novamente a nota da prova: "))