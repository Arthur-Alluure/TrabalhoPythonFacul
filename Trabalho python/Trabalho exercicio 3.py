def cachorro_peso(pergunta):   #função do peso do cachorro
    while True:
        try:   #utilizando o try dentro do loop para tratar algum erro de dado caso o usuário digite um valor não númerico
            x = int(input(pergunta))
            print('')
            if(x>=50) : #caso o valor seja maior do que o permitido
                print('Não aceitamos cachorros tão grandes')
                print('Por favor entre com o peso do cachorro novamente')
                print('')
            else:
                break
        except:       #except caso o usuario digite um valor não numerico
            print('Você digitou um valor não númerico')
            print('Por favor entre com o peso do cachorro novamente')
            print('')

    global base    #utilização do comando global em cima da variável base para retornar o valor no programa principal de acordo com o peso

    if (x<3) : #condições da variavel base
         base = 40
    elif(x>=3) and (x<10) :
         base = 50
    elif(x>=10) and (x<30) :
         base = 60
    elif(x>=30) and (x<50) :
         base = 70

    return base


def cachorro_pelo(pergunta) :              #funcao do pelo do cachrro
    print('Entre com o pelo do cachorro: ')
    print('c - Pelo Curto')
    print('m - Pelo Médio')
    print('l - Pelo Longo')
    x = input(pergunta)
    print('')
    while True: #utilização do loop infinito para validar os dados de entrada
        if (x!='c') and (x!='m') and (x!='l') :
            print('Opção de pelo inválida, digite novamente')
            x = input(pergunta)
        else:
            break

    global multiplicador   #comando global na variavel multiplicador para retornar o valor no programa principal

    if (x=='c') : #condições da variavel multiplicador
        multiplicador = 1
    elif (x=='m') :
        multiplicador = 1.5
    elif (x=='i') :
        multiplicador = 2

    return multiplicador


def cachorro_extra(pergunta) :  #funcao dos acréscimos
    while True:
        try : #try para tratar os dados de entrada do usuário
            print('Deseja adicionar mais algum serviço?')
            print('1 - Corte de unhas - R$ 10,00')
            print('2 - Escovar Dentes - R$ 12,00')
            print('3 - Limpeza de Orelhas - R$ 15,00')
            print('0 - Não desejo mais nada ')
            x = int(input(pergunta))
            print('')

            global soma_adicional        #comando global para retornar o valor da soma_adicional ao programa principal

            if (x == 0) : #condições da variavel local extra
                break
            elif (x == 1):
                extra = 10
            elif (x == 2):
                extra = 12
            elif (x == 3):
                extra = 15

            soma_adicional += extra    #variavel soma_adicional adicionar para armazenar a quantidade de acrescimos

        except: #except caso o usuario digite um valor que nao seja númerico ou que nao esteja no intervalo (1,2 ou 3)
            print('Digite uma opção de serviço válida')
            print('')

    return soma_adicional



#programa principal

base = 0
soma_adicional = 0
multiplicador = 0
total = 0

print('Bem-vindo ao Pet Shop do Arthur Rodrigues Moreira !')
cachorro_peso('Entre com o peso do cachorro: ')
cachorro_pelo('')
cachorro_extra('')
total = (base*multiplicador)+soma_adicional
print('Total a pagar(R$) : {}'.format(total))
print('(peso: {} * pelo: {} + adicional(is): {})'.format(base,multiplicador,soma_adicional))