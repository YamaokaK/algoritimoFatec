nome = input("Digite seu nome: ")

print(f"Ola, Tenha uma excelente noite {nome} !!")
print(type(nome))
print(len(nome))

for i in range(len(nome)-1, -1, -1):
    print(nome[i], end=" ")

print(end="\n")
print(nome[::-1])

novo_nome = nome.replace('a', '@').replace('A', '@')
print(novo_nome)