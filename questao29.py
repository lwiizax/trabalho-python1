numero = int(input("Digite um número inteiro positivo para calcular o fatorial: "))

if numero < 0:
    print("Número inválido. Por favor, digite um número inteiro positivo.")
else:
    fatorial = 1

    for i in range(1, numero + 1):
        fatorial *= i

    print(f"O fatorial de {numero} é: {fatorial}")