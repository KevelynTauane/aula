altura= float(input("Qual e a sua altura?: "))
peso= float(input("Qual e o seu peso?: "))
imt= peso+(altura*altura)
print("O IMT foi de")
if imt <= 18.5:
    print(f"Classificação: Abaixo do peso")
elif imt >= 18.5   >=24.9:
    print(f"Classificação: Peso normal")
elif imt >= 25.0  >=29.9:
    print(f"Classificação: Sobrepeso")
