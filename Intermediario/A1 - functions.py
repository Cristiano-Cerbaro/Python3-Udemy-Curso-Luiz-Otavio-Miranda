"""
Funções
"""


def saudacao(msg='Olá', nome='Usuario'):
    print(msg, nome)


saudacao()
saudacao('Mensagem', 'Nome')
saudacao(nome='Zezinho', msg='Olá')  # pode ser invertido os parametros, porém necessita informar


def divisao(n1, n2):
    if n2 > 0:
        return n1 / n2


print(divisao(10, 2))
