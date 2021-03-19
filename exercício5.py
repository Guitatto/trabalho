#Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#Álcool:
#até 20 litros, desconto de 3% por litro
#acima de 20 litros, desconto de 5% por litro
#Gasolina:
#até 20 litros, desconto de 4% por litro
#acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.


tipo = float(input('Qual Tipo de Aditivo voce que Adicionar 1 - Gasolina ou 2 - Alcool: '))
quantidade = float(input('informe a quantidade: '))

if tipo == 2:
    if quantidade <= 20:
        valorAlcool = quantidade * 1.90
        descontoA1 = (3 * valorAlcool) / 100
        valorAlcool = (valorAlcool -descontoA1)
        print(f'O valor a ser pago é de: {valorAlcool}')
    if quantidade > 20:
        valorAlcool = quantidade * 1.90
        descontoA2 = (6 * valorAlcool) / 100
        valorAlcool = (valorAlcool -descontoA2)
        print(f'O valor a ser pago é de: {valorAlcool}')

if tipo == 1:
    if quantidade <= 20:
        valorGasolina = quantidade * 2.50
        descontoG1 = (3 * valorGasolina) / 100
        valorGasolina = (valorGasolina -descontoG1)
        print(f'O valor a ser pago é de: {valorGasolina}')
    if quantidade > 20:
        valorGasolina = quantidade * 2.50
        descontoG2 = (6 * valorGasolina) / 100
        valorGasolina = (valorGasolina -descontoG2)
        print(f'O valor a ser pago é de: {valorGasolina}')