for i in range (1,6):
    nota= float(input("Digite a sua nota"))

if nota<20 or nota>20:
    print("Nota inválida")
elif nota<10:
    print("Insuficiente")
elif nota <14:
    print("Suficiente")
elif nota<18:
    print("Bom")
else :
    print("Muito bom")