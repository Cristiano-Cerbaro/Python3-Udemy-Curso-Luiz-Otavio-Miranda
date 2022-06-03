"""
Manipulando Strings
"""

# INDICES
texto = 'Python s2'

# positivos [012345678]
print(texto[2])
# negativos -[987654321]
print(texto[-2])
# Fatiado   :  dois pontos no meio
print(texto[2:6])  # do 2 ao 5 ( o 6 não é incluido )
print(texto[-2:-6])  # negativo
print(texto[:6])  # do inicio ao 5( o 6 não é incluido )
print(texto[7:])  # do 7 ao final

print(texto[0:6:2])  # :2 no final é step, pra pular de 2 em dois
print(texto[0::2])  # :2 no final é step, pra pular de 2 em dois
