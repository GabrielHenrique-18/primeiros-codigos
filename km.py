#gabriel henrique 
#umc
#ENTRADA DE DADOS
D=float(input("Coloque a distancia percorrida em KM:"))
L=float(input("Digite o combustivel consumido em litros:"))
#Processamento de dados
C=D/L
#saida de dados
print("a distancia percorrida foi de %.2f KM, o combustivel consumido foi de %.2f L, e o consumo medio foi de %.2f km/L" %(D,L,C))