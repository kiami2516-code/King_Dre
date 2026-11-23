positivos = 0
negativos = 0
zeros = 0

for i in range(10):
    numero = int(input(f"Introduza o {i+1}º número inteiro: "))
    
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        zeros += 1


print(f"Total de números positivos: {positivos}")
print(f"Total de números negativos: {negativos}")
print(f"Total de zeros: {zeros}")
