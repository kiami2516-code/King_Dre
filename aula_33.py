nota = float(input("Introduza uma nota (ou -1 para terminar): "))


while nota != -1:
    
    if nota < 0 or nota > 20:
        print("Nota inválida")
    elif nota <= 9:  
        print("Insuficiente")
    elif nota <= 13:
        print("Suficiente")
    elif nota <= 17:  
        print("Bom")
    else:  
        print("Muito Bom")

    
    nota = float(input("Introduza outra nota (ou -1 para terminar): "))

print("O processo terminou.")

