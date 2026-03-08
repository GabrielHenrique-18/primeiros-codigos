#gabriel henrique
#umc
#trabalho de conversao em dolar
X=float(input("coloque o valor em R$ que deseja converter: "))
D=float(input("coloque a cotaçao atual do dolar: "))
#processamento de dados
Y=X/D
Y=round(Y,2)
VFD=Y
print("A conversao de" , X, "em dolares é ", Y)