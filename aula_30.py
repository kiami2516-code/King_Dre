for i in range(1, 6):
    valor = float(input(f"Introduza o valor da {i}ª compra (€): "))
    
    if valor < 0:
        print(" Compra inválida (valor negativo).")
    else:
        
        if valor < 50:
            percentagem = 0
        elif valor < 100:
            percentagem = 5
        else:
            percentagem = 10
            
        
        desconto = valor * (percentagem / 100)
        total = valor - desconto
        
        
        print(f" Desconto aplicado: {percentagem}% ({desconto:.2f} €)")
        print(f"Total a pagar: {total:.2f} €")
    
    print("-" * 40)