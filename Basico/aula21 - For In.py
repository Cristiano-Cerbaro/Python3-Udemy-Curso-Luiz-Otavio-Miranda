"""
  For in Python
  Iterando strings com o for
  Função Range(start=0,stop,step=1
"""
texto = 'Python'
nova_string = ''

# for n, letra in enumerate(texto):
#     print(n,letra)

for n in range(5, 10, 1):
    print(n)

for n in range(15, 10, -1):
    print(n)

for letra in texto:
    if letra == 't':
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra

print(nova_string)
