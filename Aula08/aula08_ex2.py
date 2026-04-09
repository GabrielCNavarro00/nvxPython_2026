list = [11, 7, 2, 4]
menor = list[0]
for i in list:
    if i < menor:
        menor = i
print(f"O menor valor é: {menor}")