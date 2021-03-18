#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#par ou ímpar;
#positivo ou negativo;
#inteiro ou decimal.
n1 = float(input('Informe um número: '))
n2 = float(input('Informe outro número: '))
print('selecione um tipo de função: ')
soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2
funcao = int(input('(Soma 1) (subtracao 2) (multiplicacao 3) (divisao 4)'))
resultado = 0
if funcao == 1:
    resultado = n1 + n2
    print(f'A soma é: {resultado}')
if funcao == 2:
    resultado = n1 - n2
    print(f'A subtracao é: {resultado}')
if funcao == 3:
    resultado = n1 * n2
    print(f'A multiplicacao é: {multiplicacao}')
if funcao == 4:
    resultado = n1 / n2
    print(f'A divisao é: {divisao}')

if (resultado%2) == 0:
    print('resultado é par')
else:
    print('resultado é impar')

if resultado>=0:
    print('positivo')
else:
    print('negativo')

if resultado == int(resultado):
    print('inteiro')
else:
    print('decimal')

