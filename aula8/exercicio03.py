
frase = input("Digite sua frase: ")
vogal = 0
'''
for letra in frase:
    if letra.lower() == 'a':
        vogal += 1
    if letra.lower() == 'e':
        vogal += 1
    if letra.lower() == 'i':
        vogal += 1
    if letra.lower() == 'o':
        vogal += 1
    if letra.lower() == 'u':
        vogal += 1
print(vogal)

'''

for letra in frase:
    if letra.lower() in 'aeiou':
        vogal += 1

print(f"Quantidade de vogais = {vogal}")