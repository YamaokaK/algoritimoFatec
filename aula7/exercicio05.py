'''
while True:
    n = int(input('Digite o número para calcular o fatorial: '))
    i = n - 1
    soma = n
    if n > 0:
        break
    print("Valor invalído, valor tem que ser < 0 !")

while True:
    soma = soma * i
    i -=1
    if i <= 1:
        break

print(f"o Fatorial do numero é: {soma}")
'''

while True:
    n = int(input('Digite o valor a ser calculado: '))
    if n >= 0:
        break
    print("O Valor tem QUE SER MAIOR QUE 0")

if (n == 0) or (n == 1):
    fatorial = 1
else:
    fatorial = 1
    for i in range(1, n+1):
        fatorial *= i

print(f"O valor de {n}! é igual a {fatorial}")