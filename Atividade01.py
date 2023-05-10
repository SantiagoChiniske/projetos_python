print('Bem vindo a Loja do Santiago Chiniske Pereira')
#Aqui pego o valor do produto e a quantidade de produtos 
valor_produto = float(input('Digite o valor do produto: '))
qtd_produto = int(input('Quantos produtos você vai querer:'))

#Aqui eu pego o valor total do valor prduto com a quantidade 
valor_total = valor_produto * qtd_produto 

#Aqui começamos a deciçoes para qual desconto o usuário vai conseguir

if qtd_produto>= 0 and qtd_produto<= 9:
#Entre as quantidade 0 e 9, não tem direito a desconto
    print(f'Valor total sem desconto: {valor_total}')

elif  qtd_produto >= 10 and qtd_produto <= 99:
#Entre as quantidade 10e 99,tem direito a  5% desconto
    valor_desconto = valor_total* 0.05
    valor_produto_desconto = valor_total - valor_desconto
    print(f'O valor sem desconto: {valor_total}')
    print('O valor  com desconto: {0:.2f}'.format(valor_produto_desconto))

elif qtd_produto >= 100 and qtd_produto <= 999:
#Entre as quantidade 10e 99,tem direito a  10% desconto
    valor_desconto = valor_total* 0.1
    valor_produto_desconto = valor_total - valor_desconto
    print(f'O valor sem desconto: {valor_total}')
    print('O valor  com desconto: {0:.2f}'.format(valor_produto_desconto))

elif qtd_produto >= 1000:
#Entre as quantidade 1000 até o infinito,tem direito a  15   % desconto
    valor_desconto = valor_total* 0.15
    valor_produto_desconto = valor_total - valor_desconto
    print(f'O valor sem desconto: {valor_total}')
    print('O valor  com desconto: {0:.2f}'.format(valor_produto_desconto))
    
else:
#Aqui caso o usário erre a entrada de informações
    print('Valor inserido incorreto')