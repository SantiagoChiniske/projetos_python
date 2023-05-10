print('Bem vindo a Loja do Santiago Chiniske Pereira')
valor_produto = float(input('Digite o valor do produto: '))
qtd_produto = int(input('Quantos produtos você vai querer:'))

if qtd_produto>= 0 and qtd_produto<= 9:
    print('Entrou aqui')

elif  qtd_produto >= 10 and qtd_produto <= 99:
   ## valor_desconto = valor_produto * int(qtd_produto)
   ## valor_desconto = valor_produto * 0.05
    valor_desconto = valor_produto* 5/100
    valor_produto_desconto = valor_produto - valor_desconto
    print(f'valor do produto com desconto: {valor_produto_desconto:.2f}')

elif qtd_produto >= 100 and qtd_produto <= 999:
    print('Entrou aqui3')

elif qtd_produto >= 1000:
    print('Entrou aqui4')
    
else:
    print('Valor inserido incorreto')