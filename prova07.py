#encontre o maior índice de uma lista

#pedimos ao usuario para digitr uma lista, depois usamos o max() para definir o maior indice dela  
numero = input('digite alguns numeros separado por virgula: ')
lista_num = numero.split(',')
max = max(lista_num)
print(max)


# 1- peça pro usuario digitar uma lista dividida por vírgula- "123"
# 2- split pra dividir em lista - [1,2,3]
# 3- usamos o "max"  para definirmos o maior indice da lista
# 4- exibimos o resultado em tela para o usuário