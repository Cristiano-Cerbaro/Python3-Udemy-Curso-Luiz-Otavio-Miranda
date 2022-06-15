# 1 - Saudação

def saudacao(saudacao, nome):
    print(saudacao, nome)

saudacao('Bem Vindo!', 'Fulano')

# 2 - 3 numeros, e soma

def soma(n1, n2, n3):
    print(n1 + n2 + n3)


soma(1, 2, 3)


# 2 numeros, valor e percentual, retorna o valor acrescido do percentual

def percentual(valor, porcento):
    return valor + valor * porcento / 100


ap = percentual(100, 10)
print(ap)


# pizz buzz, se dividido por 3 retorna fizz, se dividido por 5, buzz, se dividido por 5 e 3, retorna FizzBuzz
# caso contrário retorne o numero

def FizzBuzz(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return 'Fizzbuzz'
    if numero % 5 == 0:
        return 'Buzz'
    if numero % 3 == 0:
        return 'Fizz'
    return numero

print(FizzBuzz(9))

from random import randint

for i in range(100):
    aleatorio = randint(0,100)
    print(FizzBuzz(aleatorio))