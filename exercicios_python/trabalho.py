#gabriel henrique
#04/03/2026
#umc
#entrada de dados
#calculo de valor do desconto de um produto
V=float(input("coloque o valor do produto em R$: "))
P=float(input("entre com a % de desconto, ex 30,35 escreva 30.25: "))
#processamento de dados
D=V*(P/100)
#saida de dados
print("o valor do produto em R$ é ", V)
print("o valor do desconto em % ", P)
print("o valor do desconto do produto é: ", D)