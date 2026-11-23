while True:
    print("\n - CALCULADORA ")
    print("1 — Adição")
    print("2 — Subtração")
    print("3 — Multiplicação")
    print("4 — Divisão")
    print("0 — Sair")
    
    
    opcao = input("Escolha uma opção: ")
    
    
    if opcao == "0":
        print("A encerrar a calculadora. Até à próxima!")
        break

        
    elif opcao in ["1", "2", "3", "4"]:
        
        try:
            num1 = float(input("Introduza o primeiro número: "))
            num2 = float(input("Introduza o segundo número: "))
        except ValueError:
            print("Erro: Por favor, introduza apenas números válidos.")
            continue
            
        
        if opcao == "1":
            resultado = num1 + num2
            print(f"Resultado: {num1} + {num2} = {resultado}")
            
        elif opcao == "2":
            resultado = num1 - num2
            print(f"Resultado: {num1} - {num2} = {resultado}")
            
        elif opcao == "3":
            resultado = num1 * num2
            print(f"Resultado: {num1} * {num2} = {resultado}")
            
        elif opcao == "4":
            
            if num2 == 0:
                print("Erro: Não é possível dividir por zero!")
            else:
                resultado = num1 / num2
                print(f"Resultado: {num1} / {num2} = {resultado}")
                
    else:
        print("Opção inválida")
        
