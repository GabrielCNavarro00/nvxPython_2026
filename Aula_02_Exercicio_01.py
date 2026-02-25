din_hora = float(input("Quanto ganha por hora: "))
hora_mes = int(input("Quantas horas trabalha por mes: "))
salario = din_hora*hora_mes
salario_liquido = (salario - salario*0.11 - salario*0.08 - salario*0.05)
print("Seu salario bruto é: ")
print("Seu IR é: ",salario*0.11)
print("Seu INSS é: ", salario*0.08)
print("Seu Sindicato é: ",salario*0.05)
print(f"Seu salario liquido é de: R$ {salario_liquido:.2f}")



