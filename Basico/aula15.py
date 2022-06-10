"""
exercicios
"""

# EXERCICIO 1
"""
numero = input("Digite um numero inteiro")

if numero.isdigit():
    numero = int(numero)
    if (numero % 2) == 0:
        print("Numero Par")
    else:
        print("Numero impar")
else:
    print("Numero digitado não é inteiro")
"""

# EXERCICIO 2 - SOLUCAO 1

"""
hora = input("Digite que horas são:")
if hora.isdigit():
    hora = int(hora)
    if hora >= 0 and hora < 12:
        print("Bom Dia ")
    elif hora >= 12 and hora < 18:
        print("Boa Tarde")
    elif hora >= 18 and hora < 24:
        print("Boa Noite")
    else:
        print('Hora Invalida')
else:
    print('Hora Invalida')
"""

# EXERCICIO 2 - SOLUCAO 2
"""
try:
    hora = int(input("Digite que horas são:"))
    if hora >= 0 and hora < 12:
        print("Bom Dia ")
    elif hora >= 12 and hora < 18:
        print("Boa Tarde")
    elif hora >= 18 and hora < 24:
        print("Boa Noite")
    else:
        print('Hora Invalida')
except:
    print("Hora Invalida")
"""

# EXERCICIO 3

nome = input("Qual o seu nome:")

if len(nome) <= 4:
    print('Seu nome é muito curto')
elif len(nome) <= 6:
    print("Seu nome é normal")
else:
    print("Seu nome é muito grande")
