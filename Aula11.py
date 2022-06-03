"""
Operadores Relecionais < > == <>
!= diferente
"""

nome = input('Qual o seu nome?')
idade = int(input('Qual a sua Idade?'))

idade_menor = 18
idade_maior = 30

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar o empréstimo')
else:
    print(f'{nome} Não pode pegar o emprestimo')

num_1 = 2
num_2 = 2
expressao = (num_2 == num_1)

print(2 == 2)  # true
print(expressao)
