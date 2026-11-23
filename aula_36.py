numero_secreto = 7
max_tentativas = 5
tentativas_utilizadas = 0
acertou = False

print(" - Jogo de Adivinhação ")
print(f"Tens {max_tentativas} tentativas para adivinhar o número secreto (entre 1 e 10).")


while tentativas_utilizadas < max_tentativas and not acertou:
    
    palpite = int(input(f"\nTentativa {tentativas_utilizadas + 1} de {max_tentativas} - Introduz o teu palpite: "))
    
    
    tentativas_utilizadas += 1
    
    
    if palpite == numero_secreto:
        acertou = True
        print(f"Parabéns! Acertaste no número secreto ({numero_secreto})!")
    elif palpite < numero_secreto:
        print("O número secreto é MAIOR do que o teu palpite.")
    else:
        print("O número secreto é MENOR do que o teu palpite.")

if acertou:
    print(f"Terminaste o jogo em {tentativas_utilizadas} tentativa(s).")
else:
    print(f"\nPerdeste! Esgotaste as {max_tentativas} tentativas.")
    print(f"O número secreto era: {numero_secreto}.")
    


