print(":::ACADEMIA FEMININA:::")
sexo=input("Informe qual é o sexo (M ou F):")
idade=int(input("Informe qual sua idade"))

if(str.upper(sexo)=='F' and idade>=18):
    print("Seu acesso está autorizado")
    
else:
    print("Você não pode acessar o estabelecimento!")