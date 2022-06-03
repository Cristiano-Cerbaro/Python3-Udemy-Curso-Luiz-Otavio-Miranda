"""
desafio aula 8
"""
nome = 'Cristiano'
idade = 33
altura = 1.72
peso = 82.5
ano_atual = 2022
nascimento = ano_atual - idade;
imc = peso / altura ** 2
print('Nome {} , idade {} , altura {} , peso {}, Ano Atual {}, Nascimento {}, IMC {:.2f}'.format(nome, idade, altura,
                                                                                                 peso, ano_atual,
                                                                                                 nascimento, imc))
print(f'Nome {nome} , idade {idade} , altura {altura} , peso {peso}, Ano Atual {ano_atual}, Nascimento {nascimento}, IMC {imc:.2f}')
