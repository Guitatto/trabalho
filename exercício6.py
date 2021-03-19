#Uma fruteira está vendendo frutas com a seguinte tabela de preços:
# #Até 5 Kg           Acima de 5 Kg
#Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
#Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.



fruta = int(input('Qual Fruta voce deseja? Morango - 1 ou Maça - 2: '))
kg = float(input('quantos quilos voce deseja? '))
motivo = input('qual o motivo? ')

if fruta == 1:
    if kg <= 5:
        valor = kg * 2.5
        if valor >= 25:
            descontoMo = (valor * 10) / 100
            valor = (valor - descontoMo)
    if kg > 5:
        valor = kg * 2.2
        if valor >= 25:
            descontoMo = (valor * 10) / 100
            valor = (valor - descontoMo)

    if kg >= 8:
        valor = kg * 2.2
        descontoMo = (valor*10) /100
        valor = (valor -descontoMo)

    valor = kg * 2.2
    if valor >= 25:
        descontoMo = (valor * 10) / 100
        valor = (valor - descontoMo)

    print(f'{valor}')

if fruta == 2:
    if kg <= 5:
        valor = kg * 1.8
        if valor >= 25:
            descontoMa = (valor * 10) / 100
            valor = (valor - descontoMa)
    if kg > 5:
        valor = kg * 1.5
        if valor >= 25:
            descontoMa = (valor * 10) / 100
            valor = (valor - descontoMa)
    if kg >= 8:
        valor = kg * 1.5
        descontoMa = (valor * 10) / 100
        valor = (valor - descontoMa)
    valor = kg * 1.5
    if valor >= 25:
        descontoMa = (valor * 10) / 100
        valor = (valor - descontoMa)

    print(f'{valor}')