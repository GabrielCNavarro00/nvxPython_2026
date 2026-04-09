cod = int(input("Digite o código do produto de 1 a 15: "))
if cod == 1:
    print("Seu alimento é do nao pericivel")
elif cod >= 2 and cod<=4:
    print("Seu alimento é pericivel")
elif cod == 5 or cod==6:
    print("Seu produto é do vestuario")
elif cod == 7:
    print("Seu produto é de higiene pessoal")
elif (cod>=8 and cod<=15):
    print("Seu produto é de limpeza ou utensilios domesticos") 
else:
    print("Produto invalido")    