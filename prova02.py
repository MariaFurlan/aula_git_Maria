#Calcular o número de elementos de uma lista, ex: [4,2,1,5,2,3,7,2,3]

list = input("escreva sua lista separando-os por vírgula:")
def contador (list):
    return (len(list.split(",")))
print(contador(list))

#1- solicitamos o uma lista ao usuário, separada por vírgula
#2- fatiamos por vírgula e contamos.
#3- exibição do resultado em tela para o usuário.

