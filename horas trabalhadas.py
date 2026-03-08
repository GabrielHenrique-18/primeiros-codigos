#gabriel henrique 
#umc
#ENTRADA DE DADOS
horas_trabalhadas=float(input("coloque aqui o total de horas trabalhadas:"))
salario_minimo=float(input("Coloque o valor do salario minimo a ser recebido:"))
#processamento de dados
Valor_hora=salario_minimo/2
salario_bruto=horas_trabalhadas*Valor_hora
imposto = salario_bruto * 0.03
pagamento=salario_bruto-imposto
print("com %.1f horas trabalhadas, e com um salario minimo de R$%.1f, o valor total a ser recebido com o imposto ja descontado, é de R$%.1f" %(horas_trabalhadas,salario_minimo,pagamento))
