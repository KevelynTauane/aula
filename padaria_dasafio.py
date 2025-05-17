inteiro_opcao=0
frances=0
integral= 0
doceLiso= 0
doceFarofa= 0
paoForma= 0
valorFrances= 0 
valorIntegral= 0
valorDoceLiso= 0
valorDoceFarofa= 0
valorForma=0
opcao=0

while opcao !=6:
    print("-----PADARIA-----")
    print("1- Pão Francês")
    print("2- Pão Integral")
    print("3- Pão Doce Liso")
    print("4- Pão Doce Farofa")
    print("5- Pão de Forma")
    print("6- Fim da compra")
    print("------------------")
    opcao=int(input("Escolha sua opção:"))
    if opcao==1:
        frances= int(input("Digite a qunatidade de pão francês que você quer: "))
        valorFrances= frances* 1.04
        
    elif opcao==2:
        integral= int(input("Digite a quantidade de pão integral que você quer: "))
        valorIntegral= integral * 1.04
        
    elif opcao==3:
        doceLiso= int(input("Digite a quantidade de pão doce liso que você quer: "))
        valorDoceLiso=doceLiso* 1.08
        
    elif opcao==4:
        doceFarofa=int(input("Digite a quantidade de pão doce Farofa que você quer: "))
        valorDoceFarofa=doceFarofa*1.11
        
    elif opcao==5:
        valorForma= int(input("Digite a quantidade de pão forma que você quer: "))
        valorForma=paoForma* 0.95
        
    elif opcao==6:
        
        break
    else:
        print("Opção inválida, tente novamente")
        
valortotal= valorFrances+valorIntegral+valorDoceLiso+valorDoceFarofa+valorForma
        
if frances>0:
    print(f"Pão Francês - quantidade: {frances}|Valor: R$ {valorFrances}")
            
if integral>0:
    print(f"Pão Integral - Quantidade: {integral}|Valor: R${valorIntegral}")
            
if doceLiso>0:
    print(f"Pão Doce Liso - quantidade:  {doceLiso}|Valor: R$ {valorDoceLiso}")
            
if doceFarofa>0:
    print(f"Pão Doce Farofa - Qauantidade: {doceFarofa}|Valor: R${valorDoceFarofa}")
            
if paoForma>0:
    print(f"Pão de Forma - Quantidade: {paoForma}|Valor R$:{valorForma}")
    print(f"Valor total da compra:R$ {valortotal}")