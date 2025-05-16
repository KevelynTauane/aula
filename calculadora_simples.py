numero1 = 0
numero2 = 0
opcao = -1
while opcao != 0:
    print("====Calculadora====")
    print("1- Somar")
    print("2- subtrair")
    print("3- Multiplicar")
    print("4- Dividir")
    print("0= Sair")
    opcao = int(input("Escolha uma opção: "))
    if opcao !=0:
       numero1= int(input("Digide um número: "))
       numero2= int(input("Digide outro número: "))
    if opcao ==1:
        resultado_soma= numero1+ numero2
        print(f"O resultado da soma é: {resultado_soma}")
    elif opcao ==2:
        resultado_subtracao = numero1-numero2
        print(f"O resultado da subtração é: {resultado_subtracao}")
    elif opcao ==3:
        resultado_multiplicacao= numero1* numero2
        print(f"O resultado da multiplicaçao é: {resultado_multiplicacao}")
    elif opcao ==4:
        resultado_divisao = numero1/numero2
        print(f"O redultado da divisao é: {resultado_divisao}")
    elif opcao== 0:
        print(f"Saindo da calculadora")