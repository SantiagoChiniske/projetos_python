#Atividade 03

#incio da função dimensoesObjeto

def dimensoesObjeto():

    while True:

        try:
            alturaObjeto = float(input('Digite a altura do objeto (cm): '))
            comprimetoObjeto = float(input('Digiteo comprimento do objeto (cm): '))
            larguraObjeto = float(input ('Digite a largura do objeto (cm):'))
        
            volumeCaixa = alturaObjeto * larguraObjeto * comprimetoObjeto

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

        except ValueError:
            print('Você digitou alguma dimensão do objeto com valor não numérica')
            print('Por favor entre com as dimensões desejadas novamente')
            continue

# fim da função dimensoesObjeto

#incio da função dimensoesObjeto

def pesoObjeto():
    
    while True:

        try:

            pesoObjeto = float(input('Digite o peso do objeto (em kg): '))
                        
            if pesoObjeto <= 0.1:
                return pesoObjeto *1
            
            elif 0.1 <= pesoObjeto < 1:
                return pesoObjeto * 1.5
            
            elif 1 <= pesoObjeto < 10:
                return pesoObjeto * 2
            
            elif 10  <= pesoObjeto < 30:
                return pesoObjeto * 3
            
            elif pesoObjeto >=   30:
                print('Não aceitamos objetos tão pesados')
                continue
            
        except ValueError:
             print('Você digitou peso do objeto com valor não numérica')

# fim da função dimensoesObjeto

#incio da função dimensoesObjeto

def rotaObjeto():
    print('teste')

# fim da função dimensoesObjeto

print('Bem Vindo a Companhia de Logística Santiago Chiniske Pereira ')

dimensão = dimensoesObjeto()
print(dimensão)
peso = pesoObjeto()
print(peso)