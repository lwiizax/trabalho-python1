numero1 = int(input('Digite um numero:' ))
numero2 = int(input('Digite um numero:' ))
numero3 = int(input('Digite um numero:' ))

maior = numero1
if numero2 > maior:
    maior = numero2
if numero3 > maior:
    maior = numero3

menor = numero1
if numero2 < menor:
    menor = numero2
if numero3 < menor:
    menor = numero3

meio = (numero1 + numero2 + numero3) - maior - menor
print(f"Numeros em ordem decrescente: {maior}, {meio}, {menor}")
