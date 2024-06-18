soma = 0
media = 0

print("Digite 5 números:")
for i in range(5):
    numero = float(input(f"Digite o {i + 1}º número: "))
    soma += numero

media = soma / 5

print(f"A soma dos números é: {soma}")
print(f"A média dos números é: {media}")