nasc = int(input("Qual seu ano de nascimento: "))
atual = int(input("Qual o ano atual: "))
idade = atual - nasc
if idade >= 16 and idade < 18:
    print(f"Pode tirar titulo de elitor mas ainda nao pode ter habilitaçao por ter {idade} anos")
if idade >= 18:
    print(f"Pode tirar CNH por possuir {idade} anos")    
