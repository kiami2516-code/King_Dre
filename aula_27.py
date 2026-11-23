for i  in range (1,6):
    idade = int(input("Qual é a sua idade ? "))

if idade<0:
    print("Idade inválida")
elif idade<=5:
    print("Entrada gratuita")
elif idade<=17:
    print("Bilhete jovem ")
elif idade<=64:
    print("Bilhete adulto")
else:
    print("Bilhete Sénior")
