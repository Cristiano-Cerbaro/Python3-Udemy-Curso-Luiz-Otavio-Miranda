"""
iterar, passar por cada um dos elementos da string
"""

frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
nova_string = ''

while contador < tamanho_frase:
    # print(frase[contador],contador)
    letra = frase[contador]

    if letra == 'r':
        nova_string += 'R'
    else:
        nova_string += letra

   # nova_string += frase[contador]
    print(nova_string)
    contador += 1
