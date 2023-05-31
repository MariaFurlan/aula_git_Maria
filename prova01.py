#assim que o usuário digitar a sua palavra, o programa retorna ela toda minuscúla, para não termos futuros problemas, e depois invertida e comparada com a palavra escrita.

palavra = input("Digite a palavra que deseja verificar:")
palavraminuscula = palavra.lower()
palavraaocontrario = palavraminuscula[::-1]
if palavra == palavraaocontrario:
    print ("SIM")
else:
    print ("NÃO")

