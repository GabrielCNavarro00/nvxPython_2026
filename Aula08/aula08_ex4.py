list = []
pares = 0
indicePar= 0
indice = 0
for i in range (5):
    num = int(input(f'digite o {i + 1}° numero: '))
    list.append(num)


for i in range(len(list)):
    if list[i] % 2 == 0:
        pares += list[i]
        indicePar += i


print(list)
print(pares)
print(indicePar)