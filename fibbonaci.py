#Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre 
# será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva 
# um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem 
# avisando se o número informado pertence ou não a sequência.#

def fib(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return n == b or n == 0

# Testando com um número
num = 34
if fib(num):
    print("faz parte da sequencia de fib")
else:
    print("não faz parte")

