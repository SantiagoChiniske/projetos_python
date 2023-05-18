#Atividade 03

#incio da função dimensoesObjeto

def dimensoesObjeto():

    while True:

        try:
            #Aqui é entrada dos valores 
            alturaObjeto = int(input('Digite a altura do objeto (cm): '))
            comprimetoObjeto = int(input('Digiteo comprimento do objeto (cm): '))
            larguraObjeto = int(input ('Digite a largura do objeto (cm):'))
        
            volumeCaixa = alturaObjeto * larguraObjeto * comprimetoObjeto

            #Aqui vai verificar qual é a dimensão e qual vai ser o valor
            if volumeCaixa <1000:
                return 10
            
            elif 1000   <= volumeCaixa < 10000:
                return 20
            
            elif 10000 <= volumeCaixa < 30000:
                return 30
            elif 30000 <= volumeCaixa < 100000:
                return 50
            elif volumeCaixa >= 100000:
                print('Não aceitamos objetos com dimensão tão grande ')
                continue

                #Aqui caso o usuário insira um valor errado ou incorreto
        except ValueError:
            print('Você digitou alguma dimensão do objeto com valor não numérica')
            print('Por favor entre com as dimensões desejadas novamente')
            continue

# fim da função dimensoesObjeto

#incio da função dimensoesObjeto

def pesoObjeto():
    
    while True:

        try:

            #entrada dos valores
            pesoObjeto = int(input('Digite o peso do objeto (em kg): '))


            #Verificar qual o valor que será multilplicado e retorna o valor
            if pesoObjeto <= 0.1:
                return 1
            
            elif 0.1 <= pesoObjeto < 1:
                return 1.5
            
            elif 1 <= pesoObjeto < 10:
                return  2
            
            elif 10  <= pesoObjeto < 30:
                return  3
            
            elif pesoObjeto >=   30:
                print('Não aceitamos objetos tão pesados')
                continue
            
            #Caso o usuário coloque um valor incorreto
        except ValueError:
             print('Você digitou peso do objeto com valor não numérica')

# fim da função dimensoesObjeto

#incio da função dimensoesObjeto

def rotaObjeto():
   
   while True:
        print ('Selecione a rota:')

        #Aqui ele vai selecionar a distância 
        rota = input ('BR - De Brasília até Rio de Janeiro \n'+
                             'BS - De Brasília até São Paulo \n'+
                             'RB - Rio de Janeiro até Brasília'+
                             'RS - De Rio de Janeiro até São Paulo\n'+
                             'SR - De São Paulo até Rio de Janeiro\n'+
                             'SB - De São Paulo até Brasília \n'+
                             '>>')
        rota  = rota.upper()# Aqui vai transformar a letras em Maiusculo automaticamente 
        
        #Verificar qual é a rota que foi seleciona e retorna o multiplicador 
        if rota == 'RS':
            return 1
        
        elif rota =='SR':
            return 1
        
        elif rota =='BS':
            return 1.2
        
        elif rota =='SB':
            return 1.2
        
        elif rota =='BR':
            return 1.5
        
        elif rota =='RB':
            return 1.5
        
        else:
            print('Você digitou uma rota que não existe')
            continue
    

# fim da função dimensoesObjeto

print('Bem Vindo a Companhia de Logística Santiago Chiniske Pereira ')
# Aqui vai rodar as funçoes e resultado final
dimensão = dimensoesObjeto()
peso = pesoObjeto()
rota = rotaObjeto()
total = dimensão * peso * rota

#Aqui vai sair o resultado total 
print('Total a pagar(R$): {} (dimensão: {} * peso: {} * rota: {})'.format(total,dimensão,peso,rota))