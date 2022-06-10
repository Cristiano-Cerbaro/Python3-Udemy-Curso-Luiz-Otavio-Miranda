"""
For / Else em python
"""

variavel = ['Luiz Otavio', 'Joãozinho','Maria']

comeca_com_j = False
for valor in variavel:
    if valor.lower().startswith('j'):
        continue
    print(valor)
else:
    print('Não existe uma palavra que começa com J')
