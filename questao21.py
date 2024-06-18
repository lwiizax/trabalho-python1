while True:
    nota = float(input("Digite uma nota entre zero e dez: "))
    if nota >= 0 and nota <= 10:
        print(f"Você digitou a nota {nota}")
        break
    else:
        print("Valor invalido. A nota deve estar entre zero e dez.")
