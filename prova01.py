#Crie um sistema em python para identificar se a palavra que o usuário enviou é um palíndromo (palíndromo é uma palavra que se pode ler, indiferentemente, da esquerda para a direita ou vice-versa)

#assim que o usuário digitar a sua palavra, o programa retorna ela toda minuscúla, para não termos futuros problemas, e depois invertida e comparada com a palavra escrita.

palavra = input("Digite a palavra que deseja verificar:")
palavraminuscula = palavra.lower()
palavraaocontrario = palavraminuscula[::-1]
if palavra == palavraaocontrario:
    print ("SIM")
else:
    print ("NÃO")

#1- solicitar informações ao usario
#2- o problema retorna nossa ela toda minuscúla, para não termos futuros problemas
#3- o programa inverte a palavra e compara com a palavra escita pelo usuário
#4- exibição em tela do resultado
