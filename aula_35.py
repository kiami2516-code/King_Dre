PIN_CORRETO = "2468"
max_tentativas = 3
tentativas_feitas = 0
autenticado = False


while tentativas_feitas < max_tentativas and not autenticado:
    
    pin_introduzido = input("Introduza o PIN: ")
    
    
    tentativas_feitas += 1
    
    
    if pin_introduzido == PIN_CORRETO:
        autenticado = True
        print("Acesso autorizado")
        print("Bem-vindo(a) ao sistema!")
    else:
        print("PIN incorreto.")
    
        tentativas_restantes = max_tentativas - tentativas_feitas
        if tentativas_restantes > 0:
            print(f"Tentativas restantes: {tentativas_restantes}")


if not autenticado:
    print("Acesso bloqueado")
    