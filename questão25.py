numero = int(input("Digite um número entre 1 e 10 para ver a tabuada: "))

if numero < 1 or numero > 10:
    print("Número inválido. Por favor, digite um número entre 1 e 10.")
else:
    print(f"Tabuada de {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} X {i} = {resultado}")