numero = int(input("Introduza um número inteiro: "))

print(f"\n  - Tabuada do {numero} ")


for i in range(1, 11):
  
  produto = numero * i

  
  if produto % 3 == 0:
    classificacao = "Múltiplo de 3"
  elif produto % 2 == 0:
    classificacao = "Par"
  else:
    classificacao = "Ímpar"

  
  print(f"{numero} x {i} = {produto} — {classificacao}")