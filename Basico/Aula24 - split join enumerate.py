"""
Split - divide a string
Join - Junta
Enumerate - Enumera as iteracoes
"""

# ENUMERATE
string = 'O Brasil é penta.'
lista = string.split(' ')

for indice, valor in enumerate(lista):
    print(indice,valor)

# JOIN
string = 'O Brasil é penta.'

string2 = ','.join(lista)


# SPLIT
string = "O Brasil é o país do futebol, o Brasil é penta"
lista_1 = string.split(' ')
lista_2 = string.split(',')

for valor in lista_1:
    print(f'A Palavra {valor} aparece {lista_1.count(valor)}x na frase')

palavra = ''
contagem = 0
for valor in lista_1:
    qtd_vezes = lista_1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print()
print(f'A palavra que apareceu mais vezes foi {palavra} {contagem}x')