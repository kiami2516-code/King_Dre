total_acumulado = 0.0


registar_outra = 'S'

while registar_outra.upper() == 'S':
    print("\n--- NOVO REGISTO DE COMPRA ---")
    
    
    valor_compra = float(input("Introduza o valor da compra (€): "))
    
    
    if valor_compra < 0:
        print("Valor inválido")
    else:
        
        if valor_compra < 50:
            percentagem_desconto = 0
        elif valor_compra < 100:
            percentagem_desconto = 5
        else:
            percentagem_desconto = 10
            
        
        valor_desconto = valor_compra * (percentagem_desconto / 100)
        total_a_pagar = valor_compra - valor_desconto
        
        
        total_acumulado += total_a_pagar
        
        
        print("\n--- RESUMO DA COMPRA ---")
        print(f"Valor da compra: {valor_compra:.2f} €")
        print(f"Desconto aplicado: {percentagem_desconto}%")
        print(f"Valor descontado: {valor_desconto:.2f} €")
        print(f"Total a pagar: {total_a_pagar:.2f} €")
    
    
    registar_outra = input("\nPretende registar outra compra? (S/N): ").strip()
    

    while registar_outra.upper() not in ['S', 'N']:
        registar_outra = input("Opção inválida. Digite 'S' para continuar ou 'N' para terminar: ").strip

print("\n=============================================")
print(f"TOTAL ACUMULADO DE COMPRAS VÁLIDAS: {total_acumulado:.2f} €")
print("=============================================")