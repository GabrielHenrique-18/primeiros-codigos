#gabriel
#05/03
#entrada de dados
EA=int(input("coloque a quantidade atual do produto no estoque: "))
P=float(input("coloque a porcentagem de aumento: "))
#processamento de dados
AP=EA+(EA*P/100)
#saida de dados
print("voce tem", EA, "unidades do produto no estoque")
print("voce tera", AP, "produtos no estoque")