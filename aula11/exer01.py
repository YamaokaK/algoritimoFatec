tupla = ()
for i in range(5):
    x = int(input(f"Digite o {i+1}o. valor: "))
    tupla = tupla + (x,)

print(tupla[::-1])
