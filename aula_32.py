contador = 0

print(" - Análise de 5 Números ")


while contador < 5:

    numero = int(input(f"\nIntroduza o {contador + 1}º número inteiro: "))
    
    
    if numero > 0:
        print("Número positivo")
    elif numero < 0:
        print("Número negativo")
    else:
        print("O número é zero")
        
    
    contador += 1


print("\nO processamento terminou.")

    