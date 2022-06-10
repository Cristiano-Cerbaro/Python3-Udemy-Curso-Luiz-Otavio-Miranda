"""
Formatacao de Valores
"""


# Sinais > bota a esquerda   < bota a direita   ^ bota no centro
num_1 = 1
print(f'{num_1:0>10}')  # formatação pra sair com 10 digitos = 0000000001

num_1 = 1
print(f'{num_1:0>10.2f}')  # formatação pra sair com 10 digitos = 00000001.00    2f casas decimais

num_2 = 1150
print(f'{num_2:0<10}')  # formatação pra sair com 10 digitos = 0001150000.00

num_1 = 1
print(f'{num_1:0^10}')  # formatação pra sair com 10 digitos = 0000100000

nome = 'Cristiano Cerbaro'
print(f'{nome:#^50}')  #pode ser usado em nome
nome_formatado = '{:@>50}'.format(nome)
print(nome_formatado)

print(nome.lower())
print(nome.upper())
print(nome.title())

