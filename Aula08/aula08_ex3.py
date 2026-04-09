list = []
for i in range (10):
    num = int(input(f'digite o {i + 1}° numero: '))
    list.append(num)
indice = 0
maior = list[0]
for v in list:
    if v > maior:
        maior = v
for ind in range(len(list)):
    if list[ind] == maior:
        indice = ind
print(f"o maior valor é {maior} e esta na posiçao {indice}")
