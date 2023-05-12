e = 0
n = int(input("Digite um número inteiro positivo: "))
for i in range(1, n+1):
    e = e + 2**i

print(f"O valor de E = {e:.2f}")