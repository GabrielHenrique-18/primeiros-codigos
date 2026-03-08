#gabriel
#05/03
#entrada de dados
V=float(input("coloque o valor da venda em R$: "))
C=float(input("coloque o custo de fabricação do produto em R$: "))
#Processamento de dados
LU=V-C
M=(LU/C)*100
M=round(M,2)
#saida de dados
print("O valor de venda do produto em R$ foi de ", V)
print("O custo de fabricação em R$ foi de ", C)
print("O lucro obtido em R$ foi de ", LU )
print("A margem de lucro em % foi de ", M )