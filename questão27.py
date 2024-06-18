numeros_pares = 0
numeros_impares = 0

print("Digite 10 números inteiros:")
for i in range(10):
    numero = int(input(f"Digite o {i + 1}º número: ")) 
    
    if numero % 2 == 0:
        numeros_pares += 1
    else:
        numeros_impares += 1
print(f"Quantidade de números pares: {numeros_pares}")
print(f"Quantidade de números ímpares: {numeros_impares}")