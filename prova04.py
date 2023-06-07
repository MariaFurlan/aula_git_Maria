#Crie um sistema que peça ao usuário uma palavra e retorne o número de vogais desta palavra.

palavra = input('digite uma palavra: ')
palavra = palavra.lower()
def leitor (palavra):
    result = {}
    vogais = 'aeiou'
    for vogal in vogais:
        if vogal in palavra:
            result[vogal] = palavra.count(vogal)
    return result
print(leitor(palavra))

#1-pedir para o usuario digitar sua palavra
#2-colocar a palavra em minusculo
#3-criar um laço de repetição que identifique as vogais
#4-junto com um laço de repetiçao que irá contar as vogais
#5-mostrar quantas vogais tem
#6-exibição das vogais e da quantidade em tela para o usuário.