total = 0       #variavel "total" vai armazenar o total a ser pago no fim, começa com 0
print('')
print('Olá, Seja Bem-Vindo a Sorveteria do Arthur Rodrigues Moreira!\n\t')
print('-'*30,'CARDÁPIO','-'*44)
print('| Nº DE BOLAS','| Sabor Tradicional (tr)', '| Sabor Premium (pr)',  '| Sabor especial (es)  |')
print('|      1     ','|      R$ 6,00          ', '|     R$ 7,00       ',  '|     R$ 8,00          |')
print('|      2     ','|      R$ 11,00         ','|     R$ 13,00     ', ' |     R$ 15,00         |')
print('|      3     ','|      R$ 15,00         ','|     R$ 18,00     ',' |     R$ 21,00         |')
print('-'*84)

while True: #inicio do loop
    sabor = input('Insira o sabor desejado (tr/pr/es): ')        #solicita o sabor, caso o mesmo não cumpra as condições do if, o pragrama retorna ('sabor inválido')

    if (sabor=='tr') or (sabor=='pr') or (sabor=='es') :          #teste variavel sabor

        numero = input('Insira o número de bolas de sorvete desejado (1/2/3): ')    #solicita o numero de bolas caso o teste da variavel seja verdadeiro

        if (numero=='1') or (numero=='2') or (numero=='3') :     #teste variavel número, caso não cumpra as condições, o programa retorna('numero de bolas invalido')

            if(numero=='1') and (sabor=='tr') :      #começam os testes de comparação entre os números e sabores
                sabor = 6
                print('Você pediu {} bola(s) de sorvete no sabor Tradicional: R$ {}'.format(numero,sabor))
            elif (numero=='1') and (sabor=='pr') :
                sabor = 7
                print('Você pediu {} bola(s) de sorvete no sabor Premium: R$ {}'.format(numero,sabor))
            elif (numero=='1') and (sabor=='es') :
                sabor = 8
                print('Você pediu {} bola(s) de sorvete no sabor Especial: R$ {}'.format(numero,sabor))
            elif (numero=='2') and (sabor=='tr') :
                sabor = 11
                print('Você pediu {} bola(s) de sorvete no sabor Tradicional: R$ {}'.format(numero,sabor))
            elif (numero=='2') and (sabor=='pr') :
                sabor = 13
                print('Você pediu {} bola(s) de sorvete no sabor Premium: R$ {}'.format(numero,sabor))
            elif (numero=='2') and (sabor=='es') :
                sabor = 15
                print('Você pediu {} bola(s) de sorvete no sabor Especial: R$ {}'.format(numero,sabor))
            elif (numero=='3') and (sabor=='tr') :
                sabor = 15
                print('Você pediu {} bola(s) de sorvete no sabor Tradicional: R$ {}'.format(numero,sabor))
            elif (numero=='3') and (sabor=='pr') :
                sabor = 18
                print('Você pediu {} bola(s) de sorvete no sabor Premium: R$ {}'.format(numero,sabor))
            elif (numero=='3') and (sabor=='es') :
                sabor = 21
                print('Você pediu {} bola(s) de sorvete no sabor Especial: R$ {}'.format(numero,sabor))

            total += sabor  #ao fim das escolhas a varivel total vai armazenar e somar os valores inseridos
            print('')
            print('Deseja comprar mais sorvetes? ')
            resposta = input('Tecle [S] para continuar ou Digite outra tecla para sair do programa: ')    #variavel resposta solicitando a continuidade do programa ou não

            if (resposta=='s') or (resposta=='S') : #teste da variavel resposta, utilizando o continue e o break
                print('')
                continue
            else:
                break
        else:
            print('Número de bolas de sorvete inválido, tente novamente!') #referente ao número de bolas inválido
            print('')
    else:
        print('Sabor inválido, tente novamente!')   #referente ao sabor inválido
        print('')
print('-'*84)
print('Obrigado por comprar conosco!')
print('O valor total a ser pago foi de: {}R$'.format(total))



