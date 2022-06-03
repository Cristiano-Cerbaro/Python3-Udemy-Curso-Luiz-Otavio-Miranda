"""
Lenght
"""

usuario = input('Insira o nome do Usuário:')
qtd_caracteres = len(usuario)

print(usuario, qtd_caracteres, type(qtd_caracteres))

if qtd_caracteres < 6:
    print('Erro, menor que 6 caracteres')

# exemplo 2
string1 = input("Digite algo")
string2 = input("Denovo")

print(f'A Quantidade total de caracteres digitado foi {len(string1) + len(string2)}')
