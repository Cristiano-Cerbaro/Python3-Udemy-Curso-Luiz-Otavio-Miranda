"""
Desafio CPF
"""

# cpf = input('Digite o CPF')
# cpf = cpf.replace('.','')
# cpf = cpf.replace('-','')
#
# cont = 0
# for i,valor in enumerate(range(10,1,-1)):
#     cont += valor * int(cpf[i])
#
# primeiro = 0 if (11 - (cont % 11)) > 9 else 11 - (cont % 11)
#
# cont = 0
# for i,valor in enumerate(range(11,2,-1)):
#     cont += valor * int(cpf[i])
#     print(cont)
# else:
#     cont += primeiro * 2
#
# segundo = 11 - (cont % 11)
#
# print(cpf[0:3],'.',cpf[3:6],'.',cpf[6:9],'-',primeiro,segundo)