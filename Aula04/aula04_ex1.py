cod = int(input("Digite o código do produto de 1 a 30: "))
if cod == 1:
    print("Seu produto é do Sul")
elif cod == 2:
    print("Seu produto é do Norte")
elif cod == 3:
    print("Seu produto é do Leste")
elif cod == 4:
    print("Seu produto é do Oeste")
elif (cod>=5 and cod<=6):
    print("Seu produto é do Nordeste")  
elif (cod>=7 and cod<=9):
    print("Seu produto é do Sudeste") 
elif (cod>=10 and cod<=20):
    print("Seu produto é do Centro-Oeste")
elif (cod>=25 and cod<=30):
    print("Seu produto é do Noroeste")                
else:
    print("Produto importado")
