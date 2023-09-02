def cadastrar_colaborador(id) : #função do cadastro
    print('-' * 24, 'MENU CADASTRAR COLABORADOR', '-' * 24)
    global id_global  #uso da função global para poder alterar os valores dentro da função
    global lista_colaboradores  #uso da função global para conseguir registrar os dados na lista

    id_global +=1  # transformando o id global em um contador para ser referencia de cada cadastro

    cadastro = {} #criando um dicionário para armazenar os dados dentro da lista
    cadastro['ID'] = id_global
    print('Id do colaborador {}'.format(id_global)) #print do id correspondente ao colaborador
    cadastro['Nome: '] = input('Por favor entre com o nome: ')   #armazenamento dos dados no dicionário
    cadastro['Setor: '] = input('Por favor entre com o setor: ')
    cadastro['Salário: '] = float(input('Por favor entre com o pagamento(R$) : '))
    lista_colaboradores.append(cadastro.copy()) #copiando dicionário para a lista

def consultar_colaborador() : #função da consulta
    while True:  # loop infinito para as opções
        try:
            print('-' * 27, 'MENU CONSULTAR COLABORADOR', '-' * 21)
            print('Escolha a opção desejada: ')
            print('1- Consultar Todos')
            print('2- Consultar por ID')
            print('3- Consultar por setor')
            print('4- Retornar ao menu')
            res = int(input(''))  # variavel res do tipo inteiro para armazenar a escolha do usuário
            print('-' * 30)
            if res not in (1, 2, 3, 4):  # caso o usuário digite um número que não esteja entre 1 a 4
                print('Opção inválida')
                continue
            if (res==1) :                     #condições de escolha das consultas
                for c in lista_colaboradores: #varredura na lista
                    print('ID: ', c['ID'])
                    print('Nome:',c['Nome: '])
                    print('Setor:',c['Setor: '])
                    print('Pagamento:',c['Salário: '])

            elif(res==2) :
                id = int(input('Digite o id do colaborador: ')) #pergunta o id do colaborador
                for i in lista_colaboradores : # varredura na lista
                    if i['ID'] == id: #se meu contador "i" quando estiver na chave 'ID' for igual ao id digitado ele faz o print das infos
                        print('ID: ', i['ID'])
                        print('Nome:', i['Nome: '])
                        print('Setor:', i['Setor: '])
                        print('Pagamento:',i['Salário: '])

            elif(res==3) :
                setor = (input('Digite o setor do colaborador: '))
                for i in lista_colaboradores:
                    if i['Setor: '] == setor:   #mesma logica da escolha anterior apenas alterando a chave de busca
                        print('ID: ', i['ID'])
                        print('Nome:', i['Nome: '])
                        print('Setor:', i['Setor: '])
                        print('Pagamento:', i['Salário: '])

            if (res==4) : #retorna ao menu
                break
        except ValueError:  # except caso o usuário digite uma letra no lugar do número
            print('Opção inválida')
            continue


def remover_colaborador(): #função da remoção
    print('-' * 28, 'MENU REMOVER COLABORADOR', '-' * 21)
    id = int(input('Digite o id do colaborador a ser removido: ')) #pergunta o id a ser removido
    for i in lista_colaboradores : #varredura da lista
        if i['ID'] == id: #caso meu contador 'i' na chave do 'ID' seja correspondente ao id digitado ele remove o mesmo
            lista_colaboradores.remove(i)



#programa principal

lista_colaboradores = []
id_global = 0
print('Bem vindo ao Controle de Colaboradores do Arthur Rodrigues Moreira')
print('*'*76)
while True: #loop infinito para as opções
    print('')
    print('-' * 30, 'MENU PRINCIPAL', '-' * 30)
    try:
        print('Escolha a opção desejada: ')
        print('1- Cadastrar Colaborador')
        print('2- Consultar Colaborador(es)')
        print('3- Remover Colaborador')
        print('4- Sair')
        res = int(input(''))   #variavel res do tipo inteiro para armazenar a escolha do usuário
        if res not in (1,2,3,4) :  #caso o usuário digite um número que não esteja entre 1 a 4
            print('Opção inválida')
            continue #retona ao loop
    except ValueError: #except caso o usuário digite uma letra no lugar do número
        print('Opção inválida')
        continue #retorna ao loop

    if (res==1) :
        cadastrar_colaborador(id_global) #caso 1, o programa vai para a função cadastro com o parâmetro do id global
    elif (res==2) :
        consultar_colaborador() #caso2, programa vai para função de consulta
    elif (res==3) :
        remover_colaborador() #caso 3, programa vai para a função de remover

    elif (res==4) :   #loop se encerra
        break




