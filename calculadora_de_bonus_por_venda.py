nome_vendedor = float(input("Digite o nome do vendedor"))
salario_fixo = float(input("Digite o salario fixo"))
total_vendas = float(input("Digite o total de venda"))
comissao = 0.15
if total_vendas >=20:
    comissao <= salario_fixo * 15
    salario_recebido = salario_fixo + comissao
    print("Salario recebido")
elif total_vendas <= 20:
    print("Salario recebido")