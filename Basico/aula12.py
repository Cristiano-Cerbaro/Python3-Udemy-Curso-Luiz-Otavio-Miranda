"""
Operadores Lógicos
and, or , not, in e not in
"""
a = 0
b = 2
c = 3
# a == b and b < c
# 0 é considerado falso/sem valor no NOT
if not a:
    print('Informe A')

nome = 'Cristiano'

if 'a' in nome:
    print('Tem A no nome')
elif 'asas' not in nome:
    print('Não tem no nome')
