#Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.
num = float(input('Informe um número qualquer: '))
if int(num) == num:
    print('número Inteiro')
else:
    print('é um número Decimal')