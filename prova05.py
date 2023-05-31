#atribuímos uma lista com valores de 50 à 200, criamos um laço e repetição que conta a partir de 51 de dois em dois números.S
lista = list(range(50,200))
for valor in lista:
    if valor % 2 != 0:
        print(valor)