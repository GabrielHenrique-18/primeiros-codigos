#gabriel henrique 
#umc
#entrada de dados
NAS=int(input("insira o seu ano de nascimento:"))
ATU=int(input("insira o ano atual:"))
#processamento de dados
IDA=ATU-NAS                                         #IDA=Idade atual
ID30=2030-NAS                                       #ID30=Idade em 2030
#SAIA DE DADOS
print("o seu ano de nascimento é %i, e o ano atual é %i. Logo a sua idade atual é de %i anos , e em 2030 voçe tera %i anos" %(NAS,ATU,IDA,ID30))