lista = []
menor = lista[0]
gerador = int(input('Digite a quantidade de elementos: '))
for i in range (gerador):
    num = int((input(f'digite o {i + 1}° numero: ')))
    lista.append(num)
print('numeros:', lista)
print
