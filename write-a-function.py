""" 
Um dia extra é adicionado ao calendário quase a cada quatro anos como 29 de fevereiro, e esse dia é chamado de dia bissexto. Ele corrige o calendário para o fato de que nosso planeta leva aproximadamente 365,25 dias para orbitar o sol. Um ano bissexto contém um dia bissexto.

No calendário gregoriano, três condições são usadas para identificar anos bissextos:

O ano pode ser dividido igualmente por 4, é um ano bissexto, a menos que:
O ano pode ser dividido igualmente por 100, NÃO é um ano bissexto, a menos que:
O ano também seja divisível por 400. Então, é um ano bissexto."""

def is_leap(year):
    leap = False
    if year % 4 == 0:       # verifica a possibilidade do ano ser bisexto
        if year % 100 != 0: # se o ano nâo for divisivel por 100, ele é bisexto
            return True     # retorna True quando as duas validações acima forem verdadeiras 
        else:
            return year % 400 == 0   # verifica se o ano dividido por 400 terá resto 0
    return leap

year = int(input("Year: "))
print(is_leap(year))