def calculadora():
    # escolhe a operação matematica para realizar o calculo.
    operacao = input('''
Digite a operação matematica que deseja:
+ para adição
- para subtração
* para multiplicação
/ para divição
% para porcentagem
''')

    num_1 = int(input('Digite o primeiro número: '))
    num_2 = int(input('digite o segundo número: '))

    if operacao == '+':
        print('{} + {} = '.format(num_1, num_2))
        print(num_1 + num_2)

    elif operacao == '-':
        print('{} - {} = '.format(num_1, num_2))
        print(num_1 - num_2)

    elif operacao == '*':
        print('{} * {} = '.format(num_1, num_2))
        print(num_1 * num_2)

    elif operacao == '/':
        print('{} / {} = '.format(num_1, num_2))
        print(num_1 / num_2)

    elif operacao == '%':
        print('{} % {} = '.format(num_1, num_2))
        print(num_1 % num_2)

    else:
        print('Você não digitou um operador válido, por favor tento novamente.')

    # pergunta se deseja fazer outro calculo.
    retornar()


def retornar():
    calc_novo = input('''
Deseja calcular novamente?
digite S para sim ou N para não.
''')

    if calc_novo.upper() == 'S':
        calculadora()
    elif calc_novo.upper() == 'N':
        print('até mais.')
    else:
        print('digite apenas S ou N')
        retornar()


calculadora()
