salario_inicial = 1000.00
ano_contratacao = 1995

ano_atual = 2023
percentual_aumento = 0.015

for ano in range(ano_contratacao + 1, ano_atual + 1):
    salario_inicial *= (1 + percentual_aumento)
    percentual_aumento *= 2

print(f"O salário atual do funcionário em {ano_atual} é R$ {salario_inicial:.2f}")