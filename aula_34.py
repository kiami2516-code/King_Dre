idade = int(input("Introduza a sua idade: "))


while idade < 0 or idade > 120:
    print("Erro: A idade introduzida é inválida. Deve estar compreendida entre 0 e 120 anos.")
    idade = int(input("Introduza novamente a sua idade: "))


if idade < 13:
    categoria = "Criança"
elif idade <= 17:
    categoria = "Adolescente"
elif idade <= 64:
    categoria = "Adulto"
else:
    categoria = "Sénior"


print(f"Idade válida ({idade} anos). Categoria correspondente: {categoria}.")