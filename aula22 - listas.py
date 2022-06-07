"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""

#  Jogo de Forca
secreto = 'perfume'
digitadas = []

while True:  # Laço infinito
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Isso não vale, digite uma letra apenas.')
        continue

    digitadas.append(letra)  # inclui a letra na lista

    if letra in secreto:
        print(f'Acertou, a letra {letra} existe na palavra secreta')
    else:
        print(f'ERROU, a letra {letra} não existe na palavra secreta')
        digitadas.pop()  # remove da lista dos digitadas

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Parabéns, voce acertou!!! A palavra era {secreto_temporario}')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

#     0 1 2 3 4 5 6 7 8
# l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# for a in l2:
#     print(f' O Tipo de {a} é {type(a)}')

# print(l2)
# l2.insert(0, 'Banana')
# print(l2)
# del (l2[0])
# print(l2)

# print(max(l2))  # maximo
# print(min(l2))  # minimo

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
#
# l3 = l1 + l2  # concatena
# l1.extend(l2)  # concatena / extende
# l2.append('b')  # adiciona o dado
#
# print(l3)

# lista = [1,2,3,4]
#
# #          0   1   2   3   4
# lista2 = ['A','B','C','D','E']
# #       -  5   4   3   2   1
#
# print(lista2[1:4])
# print(lista2[:4])
# print(lista2[::-1])
#
#
# lista2[3] = 'mudando valor'
