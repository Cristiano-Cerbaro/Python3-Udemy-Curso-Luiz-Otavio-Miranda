nome = 'Luiz Otávio'
print(nome, type(nome))
idade = 32
altura = 1.72
e_maior = idade > 18
peso = 82
imc = peso / altura ** 2

print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{} tem {} anos de idade e seu imc é {:.2f}'.format(nome, idade, imc))
print('{0} tem {1} anos de idade e seu imc é {2:.2f}'.format(nome, idade, imc))
print('{im} tem {n} anos de idade e seu imc é {i:.2f}'.format(im=nome, n=idade, i=imc))

print('Nome: ', nome)
print('Idade: ', idade)
print('Altura: ', altura)
print('é Maior: ', e_maior)
print(imc)