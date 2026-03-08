#gabriel henrique
#umc 
6/3
#entrada de dados
#calculo de tempo de download de um arquivo
A=float(input("coloque o tamanho do arquivo em MB, ex para 20GB coloque 20000: "))
V=float(input("Coloque a velocidade da conexão em bits por segundo:" ))
#processamento de dados
T=A/V
#saida de dados
print("o tamanho do seu arquivo é %.2f, a velocidade da sua conexão é %.2f, e o tempo de downloading é de %.2f" %(A,V,T))