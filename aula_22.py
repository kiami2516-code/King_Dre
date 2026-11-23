valor_da_casa = float(input("Digite o valor da casa : "))
salario_comprador = float(input("Digite o seu salário : "))
tempo = int(input("A quanto tempo deseja pagar a casa : "))

numero_total_meses = 10
prestação_mensal = valor_da_casa/numero_total_meses
print(prestação_mensal)
limite_perdido = salario_comprador*0.30
print(limite_perdido)

if(prestação_mensal>limite_perdido):
    print(f"Empréstimo negado, porque compromete demasiado ao orçamento mensal ")
else:
    print(f"Empréstimo aprovado ")

