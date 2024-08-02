print("""
Loja de Perfume:
      Código:       Condição de Pagamento:              Desconto:
      1.            À vista(em espécie)                 15%
      2.            Cartão de débito                    10%
      3.            Cartão de crédito(vencimento)       5%
""")

while True:
    
    tv = float(input("Informe o valor total da venda\n'0' para Finalizar "))
    if tv == 0:
        print("Finalizado")
        break
    fp = int(input("Informe a forma de pagamento: "))

    if fp == 1:
        print(f"O valor final a ser pago é: {tv * 0.85}")
    elif fp == 2:
        print(f"O valor final a ser pago é: {tv * 0.90}")
    elif fp == 3:
        print(f"O valor final a ser pago é: {tv * 0.95}")
    else:
        print("Forma de pagamento não encontrada")