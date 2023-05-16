print('Bem vindo a Lanchonete do Santiago Chiniske Pereira')
print(28*'*'+'Cardápio'+27*'*')
print('|'+4*' '+'Código'+ 3*' ' +'|' +8*' '+'Descrição'+20*' '+'|'+2*' '+'Valor'+2*' '+'|')
print('|'+5*' '+'100'+ 5*' ' +'|' +8*' '+'Cachorro Quente'+14*' '+'|'+2*' '+'9,00'+3*' '+'|')
print('|'+5*' '+'101'+ 5*' ' +'|' +8*' '+'Cachorro Quente Duplo'+8*' '+'|'+2*' '+'11,00'+2*' '+'|')
print('|'+5*' '+'102'+ 5*' ' +'|' +8*' '+'X-Egg'+24*' '+'|'+2*' '+'12,00'+2*' '+'|')
print('|'+5*' '+'103'+ 5*' ' +'|' +8*' '+'X-Salada'+21*' '+'|'+2*' '+'12,00'+2*' '+'|')
print('|'+5*' '+'104'+ 5*' ' +'|' +8*' '+'X-Bacon'+22*' '+'|'+2*' '+'14,00'+2*' '+'|')
print('|'+5*' '+'105'+ 5*' ' +'|' +8*' '+'X-Tudo'+23*' '+'|'+2*' '+'17,00'+2*' '+'|')
print('|'+5*' '+'200'+ 5*' ' +'|' +8*' '+'Refrigerenta Lata'+12*' '+'|'+2*' '+'5,00'+3*' '+'|')
print('|'+5*' '+'210'+ 5*' ' +'|' +8*' '+'Chá Gelado'+19*' '+'|'+2*' '+'4,00'+3*' '+'|')
print(64*'*')
acumulador = 0
while True:
    ...
    codigo = input('Insira o código desejado: ')

    if codigo == '100':
        print('Você pediu um Cachorro Quente no valor de 9,00')
        acumulador = acumulador + 9

    elif codigo == '101':
        print('Você pediu um Cachorro Quente Duplo no valor de 11,00')
        acumulador = acumulador + 11

    elif codigo == '102':
        print('Você pediu um X-Egg no valor de 12,00')
        acumulador = acumulador + 12

    elif codigo == '103':
        print('Você pediu um X-Salada no Valor de 12,00')
        acumulador = acumulador + 12

    elif codigo == '104':
        print('Você pediu um X-Bacon no Valor de 14,00')
        acumulador = acumulador + 14

    elif codigo == '105':
        print('Você pediu um X-Tudo no valor de 17,00')
        acumulador = acumulador + 17

    elif codigo == '200':
        print('Você pediu um Refrigerante no Valor de 5,00')
        acumulador = acumulador + 5

    elif codigo == '201':
        print('Você pediu um Chá Gelado no Valor de 4,00')
        acumulador = acumulador + 4

    else:
        print('Opção Inválida!')
        continue

    
