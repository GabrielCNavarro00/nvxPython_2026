altura = float(input("Qual sua altura em metros: "))
sexo = input("Qual seu sexo? Digite M para Masculino e F para Feminino: ").upper()
while sexo not "M" and not "F":
    print ("Sexo invalido, digite apenas M ou F")
    sexo = input("Qual seu sexo? Digite M para Masculino e F para Feminino: ").upper()
if sexo == "M": 
    print(f"Você é homem e seu peso ideal é: {(72.7*altura)-52:.2f}")
elif sexo == "F":
    print(f"Você é mulher e seu peso ideal é: {(62.1*altura)-44.7:.2f}")
    