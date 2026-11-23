distancia = float(input("Qual é o valor da distância em Km ? "))
if(distancia<=200):
 preco_km = 0.50
 print()
else:
 preco_km = 0.45

 preco_total = distancia*preco_km
 print(preco_total)

