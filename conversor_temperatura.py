
print ("====Conversor de temperatura====")
print("Escreva a temperatura em Celcius e escolha para qual deseja converter.")
print ("1- Fahrenheit")
print ("2- kelvin")
opcao = int(input("Escolha o tipo de temperatura: "))
if opcao == 1:
    print("Você escolheu Fahrenheit")
    temp_inicial= float(input("Digite sua temperatura em Celciuis: "))
    temp_convertida = (temp_inicial *9/5) +32
    print(f"O resultado em Fahrenheit é : {temp_convertida:.2f}")
elif opcao==2:
    print("Você escolheu Kelvin")
    temp_inicial= float(input("Digite sua temperatura em Celciuis: "))
    temp_convertida = temp_inicial + 273.15
    print(f"O resultado em Kelvin é : {temp_convertida:.2f}")
    