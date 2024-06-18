numero_str = input("Digite um número: ")

if '.' in numero_str:
    print(f"O número {numero_str} é decimal.")
else:
    print(f"O número {numero_str} é inteiro.")