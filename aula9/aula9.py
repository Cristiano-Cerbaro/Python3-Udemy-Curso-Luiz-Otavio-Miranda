"""
Entrada de Dados
"""
nome = input("Qual seu nome?")
idade = input("Qual sua idade?")
#idade = int(input("Qual sua idade?"))

ano_nascimento = 2022 - int(idade)

print()
print(f'{nome} tem {idade} anos. \n'
      f'{nome} nasceu em {ano_nascimento}.')
