"""
While
"""
while True:
    print()
    num_1 = input('Digite um numero:')
    num_2 = input('Digite um numero:')
    operador = input('Digite um operador:')
    sair = input('Deseja Sair? [s]im ou [n]ão:')

    if sair == 's':
        break  # sai do loop geral

    # checa se algum não é numero
    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um número')
        continue  #  retorna ao inicio do laço

    num_1 = int(num_1)
    num_2 = int(num_2)

    # + - * /
    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '/':
        print(num_1 / num_2)
    if operador == '*':
        print(num_1 * num_2)

"""
x = 0
while x < 100:

    #  pular o numero 3
    if x == 3:
        x = x + 1
        continue  # ele pula o restante das instruções do laco com essa funcao

    if x == 8:
        x = x + 1
        break  # ele quebra o laço while, e sai dele

    print(x)
    x = x + 1
"""