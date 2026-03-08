#gabriel henrique 
#UMC
#ENTRADA DE DADOS
print("""
=================================
   CONVERSOR DE SEGUNDOS
=================================
""")
segundos=int(input("coloque aqui os segundos que voçe deseja converter em minutos e segundos:"))
#processamento de dados
minutos=segundos//60
segundos_restantes=segundos%60
#saida de dados
print("%i segundos é igual á %i minutos e %i segundos." %(segundos,minutos,segundos_restantes))