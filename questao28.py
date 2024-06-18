n = int(input("Digite o número de termos da série de Fibonacci que você deseja gerar: "))

fibonacci = [1, 1]

for i in range(2, n):
    proximo_termo = fibonacci[i - 1] + fibonacci[i - 2]
    fibonacci.append(proximo_termo)

print(f"Série de Fibonacci até o {n}º termo:")
for numero in fibonacci:
    print(numero, end=" ")