"""
Conversões
"""

a = input("Digite um nro")
b = input("Digite um nro")

print(a + b)

print(a.isnumeric())
print(b.isnumeric())

if a.isdigit() and b.isdigit():
    a = int(a)
    b = int(b)

    print(a+b)
else:
    print("Não pude converter os numeros pra somar")