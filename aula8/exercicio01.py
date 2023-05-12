
nome1 = input("Digite seu primeiro nome: ")
nome2 = input("Digite seu nome do meio: ")
nome3 = input("Digite seu sobrenome: ")
nome_completo = nome1 +" " + nome2 + " " + nome3
nome_cripto = ''
for i in range(0, len(nome_completo)):
    nome_cripto = nome_cripto + chr(ord(nome_completo[i])+1)

print(f"Seu nome Criptografado é: {nome_cripto}")