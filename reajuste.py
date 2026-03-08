#gabriel henrique 
#umc
#entrada de dados
#calculo de aumento de uma aplicação em porcentagem
S=float(input("coloque o saldo atual da aplicação:"))
P=float(input("coloque a porcentagem de aumento, ex para 30,25 escreva 30.25:"))
#Processamento de dados
PC=P/100
AU=S*PC #PC= PORCENTAGEM CONVERTIDA
T=AU+S
#saida de dados
print("o saldo atual da sua aplicaçao é de %.2F, a porcentagem de aumento é %.2F, seu aumento sera de %.2F, entao sua nova aplicação sera de %.2F" %(S,P,AU,T))