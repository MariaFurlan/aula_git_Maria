#exiba em tela os números ímpares de 50 a 200 em python

#atribuímos uma lista com valores de 50 à 200, criamos um laço e repetição que conta a partir de 51 de dois em dois números.S
lista = list(range(50,200))
for valor in lista:
    if valor % 2 != 0:
        print(valor)

#1- atríbuimos uma lista de 50 a 200
#2- atribuímos um valor a lista utilizando o "for"
#2.1- criamos um laço de repetição que divide esse valor or 2, e se o resultado for diferente de 0, printamos
#3- exibição do resultado obtido em tela para o usuário.
         