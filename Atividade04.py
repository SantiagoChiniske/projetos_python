#Atividade 04

#------Início das variáveis globais-----
lista_pecas = []
codigo_pecas = 000
#------Fim das variáveis globais-----


#------Início das Cadastrar peça-----
def cadastrar_peca(codigo):
    print('Você selecionou a Opção de Cadastrar Peça')
    print('Codigo da Peça: {}'.format(codigo)) #Aqui já vai mostrar o código do produto

    #As informações que o usuário vai inserir
    nome = input('Por favor entre com o NOME da peça:')
    fabricante = input('Por favor entre com o FABRICANTE da peça:')
    preco = int(input('Entre com o VALOR(R$) do produto:'))

    # Aqui é aonde vai ser armazenado as informações
    dicionario_peca = {
        'codigo': codigo,
        'nome': nome,
        'fabricante': fabricante,
        'preco': preco
    }
    lista_pecas.append(dicionario_peca.copy())
#------Fim das Cadastrar peça-----

#------Início das Consulta peça-----
def consulta_peca():
    print('Você Selecionou a opção de Consultar Peças')
    
    while True:
        opcao_consulta = input('\nEscolha a opção desejada: \n'+
                                    '1- Consultar TODOS as peças \n'+
                                    '2- Consultar Peças por CÓDIGO\n'+
                                    '3- Consultar Peças por FABRICANTE\n'+
                                    '4-Retornar\n'+
                                    '>>')
        
        if opcao_consulta == '1':
                print('Você escolheu a opção consultar TODOS os produtos')
                for produto in lista_pecas: #Produto vai varrer toda a lista de produto
                    print('------------------------------')
                    for key,values in produto.items():# Varrer todos  oso conjutos chaves e valor do dicionario produto
                        print('{} :  {}'.format(key,values))
                    print('------------------------------')
                    
        elif opcao_consulta== '2':
            print('Você escolheu a opção consultar produtos por CÓDIGO')
            valor_desejado = int(input('Entre com CÓDIGO desejado: '))

            for produto in lista_pecas:
                if produto['codigo'] == valor_desejado: #o valor do campo codigo desse dicionario é igual o valor desejado 
                        print('------------------------------')
                        for key,values in produto.items():# Varrer todos  oso conjutos chaves e valor do dicionario produto
                            print('\n{} :  {}'.format(key,values))
                        print('------------------------------')
            
    
        elif opcao_consulta== '3':
                print('Você escolheu a opção consultar por FABRICANTE')
                valor_desejado = input('Entre com FABRICANTE desejado: ')

                for produto in lista_pecas:
                    if produto['fabricante'] == valor_desejado: #o valor do campo codigo desse dicionario é igual o valor desejado 
                        print('------------------------------')
                        for key,values in produto.items():# Varrer todos  oso conjutos chaves e valor do dicionario produto
                            print('\n{} :  {}'.format(key,values))
                        print('------------------------------')

        elif opcao_consulta== '4':
            return #Sai da função consultar_produto e volta para o amin

        else:
                print('Opção inválida. tente novamente')
                continue
#------Fim das Consulta peça-----

#------Início das Remover peça-----
def remover_peca():

    print('Bem vindo ao menu de Remover Produtos')
    valor_desejado = int(input('Entre com CÓDIGO do produto que deseja remover: '))

    for produto in lista_pecas:
               if produto['codigo'] == valor_desejado: #o valor do campo codigo desse dicionario é igual o valor desejado que será removido
                    lista_pecas.remove(produto)
                    print('Produto Removido')
#------Fim das Remover peça-----

#------Início do main-----
print('Bem vindo ao Controle de Estoque da bicicletaria do Santiago Chiniske Pereira')
while True:
    opcao_principal =input('\nEscolha a opção desejada: \n'+
                            '1- Cadastra Peças \n'+
                            '2- Consultar Peças\n'+
                            '3- Remover Peças\n'+
                            '4-Sair \n'+
                            '>>')

    #Verificar qual ele vai selecionar 
    if opcao_principal == '1':
            codigo_pecas = codigo_pecas + 1
            cadastrar_peca(codigo_pecas)

    elif opcao_principal == '2':
        consulta_peca()

    elif opcao_principal == '3':
        remover_peca()

    elif opcao_principal == '4':
        break

    else:
        print('Opção inválida. tente novamente')
        continue
#------Fim do main-----