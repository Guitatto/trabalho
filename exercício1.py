#Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).
numero = int(input('Informe um número: '))
resultado = numero % 2
if resultado == 0:
    print('O número {} é PAR'.format(numero))
else:
    print('O número {} é IMPAR'.format(numero))