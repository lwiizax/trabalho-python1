gph = float(input("Entre com o sei ganho por hora: "))
horast = float(input("Entre com suas horas trabalhadas no mês: "))

salario_bruto = gph * horast
imposto_renda = salario_bruto * 0.11
inss = salario_bruto *0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - imposto_renda - inss - sindicato

print("+ Sálario Bruto: R$", salario_bruto)
print("- IR (11%): R$", imposto_renda)
print("- INSS (8%): R$", sindicato)
print(" = Sálario Líquido: R$", salario_liquido)