salario = float(input("Qual seu salario: R$ "))
if salario >= 1250:
    salarionovo = salario * 1.1
else:
    salarionovo = salario * 1.15 
print (f"Seu novo salario será de: R$  {salarionovo:.2f}")