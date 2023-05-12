'''
while True:
    base = int(input("Digite o valor da base: "))
    altura = int(input("Digite o valor da altura: "))
    if base > 0 and altura > 0:
        break

area = (base * altura) / 2
print(f"A Area do triangulo é de:{area:.1f} ")
'''

base = float(input("Digite a base do triangulo: "))
while base <= 0:
    base = float(input("Digite a base do triangulo > 0 :"))

while True:
    altura = float(input("Digite a altura do triangulo: "))
    if altura > 0:
        break

area = (base * altura) /2

print(f"A area do triangulo é de : {area:.2f}")