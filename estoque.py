#gabriel henrique 
#umc
#05/03
#entrada de dados
#calculo de valor total do estoque
N=int(input("Coloque a quantidade do produto que voçe tem: "))
VU=float(input("coloque o valor unitario do produto, ex para R$30,25 escreva 30.25: "))
#processamento de dados
VE=N*VU
#saida de dados
print("voçe tem" , N, "produtos")
print("O valor unitario do produto em R$ é ", VU)
print("o valor total do estoque em R$ é ", VE)