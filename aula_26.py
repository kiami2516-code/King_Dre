for dia in range (1,8):
    temperatura = float(input("Digite  a temperatura : "))
    
    if temperatura < 10:
        classificacao = "frio"
    elif temperatura < 20:
        classificacao = "Aumeno"
    elif temperatura < 30:
        classificacao = "Quente"
    else:
        classificacao = "Muito Quente"

        print("Dia",dia, "-",temperatura,"ªC - ",classificacao ) 
        
