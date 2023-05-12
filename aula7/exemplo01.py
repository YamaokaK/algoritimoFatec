soma = 0
for x in range(1,11):
    idade = int(input(f"Digite a {x}a. idade: "))
    soma = soma + idade

media = soma / x
print(f"A media das idade é igual 2a: {media:.2f}")