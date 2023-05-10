print('Bem vindo a Loja do Santiago Chiniske Pereira')
valor_produto = float(input('Digite o valor do produto: '))
qtd_produto = int(input('Quantos produtos você vai querer:'))

valor_total = valor_produto * qtd_produto 

if qtd_produto>= 0 and qtd_produto<= 9:
    print(f'Valor total sem desconto: {valor_total}')

elif  qtd_produto >= 10 and qtd_produto <= 99:

    valor_desconto = valor_total* 0.05
    valor_produto_desconto = valor_total - valor_desconto
    print(f'O valor sem desconto: {valor_total}')
    print('O valor  com desconto: {0:.2f}'.format(valor_produto_desconto))

elif qtd_produto >= 100 and qtd_produto <= 999:
    valor_desconto = valor_total* 0.1
    valor_produto_desconto = valor_total - valor_desconto
    print(f'O valor sem desconto: {valor_total}')
    print('O valor  com desconto: {0:.2f}'.format(valor_produto_desconto))

elif qtd_produto >= 1000:
    valor_desconto = valor_total* 0.15
    valor_produto_desconto = valor_total - valor_desconto
    print(f'O valor sem desconto: {valor_total}')
    print('O valor  com desconto: {0:.2f}'.format(valor_produto_desconto))
    
else:
    print('Valor inserido incorreto')