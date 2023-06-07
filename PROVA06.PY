#valide se uma lista está na forma crescente ou decrescente

lista = input("digite sua lista:")  
list = lista.split(",") 
primeiro = True 
numero_anterior = 0
crescente = True 
for i in list:
    if primeiro == True:
        primeiro = False
        numero_anterior = i      
    else:
        if i != numero_anterior and i < numero_anterior:
            crescente = False

        
if crescente == True:
    print("crescente")
else:
    print("decrescente")



# 1 - solicitar informações para o usuario
# 2 - Tratativa do problema
# 2.1 - validamos o primeiro indice
# 2.2 - criamos uma variavel que valida crescente como true
# 2.3 - criamos um laço de repetição 
# 2.4 - validamo se é o primeiro indice
# 2.5 - verifica se o proximo numero é igual ao anterior
# 2.6 - verifica se o indice é menor que o numero anterior
# 2.7 - valida a nossa variavel como "crescente" ou decrescente 
# 3 - exibição em tela do resultado obtido