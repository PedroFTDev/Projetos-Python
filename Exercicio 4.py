contador1 = 0
contador2 = 0
contador3 = 0
contador4 = 0
num=0
while(num>=0):
    num=int(input("Digite um numero:"))
    if(num>=0 and num<=25):
        contador1 = contador1+1
    elif(num>=26 and num<=50):
        contador2=contador2+1
    elif(num>=51 and num<=75):
        contador3=contador3+1
    elif(num>=76 and num<=100):
        contador4=contador4+1

print("Valores entre [0-25]:",contador1)
print("Valores entre [26-50]:",contador2)
print("Valores entre [51-75]:",contador3)
print("Valores entre [76-100]:",contador4)