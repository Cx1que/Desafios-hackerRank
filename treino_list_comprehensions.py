lista_precos = [500, 1500, 2000, 100, 25]

#caso 1
nova_lista_precos = []

for preco in lista_precos:
	nova_lista_precos.append(preco*2)
print(nova_lista_precos)

# com list comprehensions
nova_lista_precos2 = [preco * 2 for preco in lista_precos]
print(nova_lista_precos2)


#caso 2
imposto = []
for preco in lista_precos:
    if preco >= 1000:
        imposto.append(preco * 0.50)

print(imposto)

# com list comprehensions
imposto = [preco * 0.50 for preco in lista_precos if preco > 1000]
print(imposto)