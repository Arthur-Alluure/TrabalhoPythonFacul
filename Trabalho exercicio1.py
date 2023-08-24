print('Olá! Seja Bem-vindo a Loja do Arthur Rodrigues Moreira')

produto = float(input('Informe o valor do produto: '))
quantidade = int(input('Informe a sua quantidade : '))
valor = produto*quantidade

#começam os testes na variavel quantidade
if (quantidade<200) :
    desconto = valor   #abaixo de 200 unidades não temos desconto, então a variavel desconto pode somente receber o valor do produto
else:
    if (quantidade>=200) and (quantidade<1000) :
        desconto = valor - (valor*0.05)  #calculo com 5% de desconto

    elif (quantidade>=1000) and (quantidade<2000) :
        desconto = valor - (valor*0.10)  #calculo com 10% de desconto

    elif (quantidade>=2000) :
        desconto = valor - (valor*0.15)  #calculo com 15% de desconto

print('O valor SEM desconto: R${}'.format(valor))
print('O valor COM desconto: R${}'.format(desconto))

#final do codigo mostrando os valores com e sem desconto
