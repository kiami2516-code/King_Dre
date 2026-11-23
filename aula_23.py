quantidade_kmw = float(input("Qual é o valor da quantidade de kmw consumidos? "))
tipo = input("Qual é o tipo de instalação (r para residencial, c para comercial e i para industrial): ")


preco_total = 0

if tipo == "r":
    if quantidade_kmw <= 500:
        preco_total = quantidade_kmw * 0.40
    else:
        preco_total = quantidade_kmw * 0.65
         
elif tipo == "c":    
    if quantidade_kmw <= 1000:
        preco_total = quantidade_kmw * 0.55
    else:
        preco_total = quantidade_kmw * 0.60

elif tipo == "i":
    if quantidade_kmw <= 5000:
        preco_total = quantidade_kmw * 0.55
    else: 
        preco_total = quantidade_kmw * 0.60
else:
    print("Tipo de instalação inválido!")


print(f"O preço a pagar é de {preco_total:.2f}€")





       


    