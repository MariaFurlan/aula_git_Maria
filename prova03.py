#Crie um sistema que peça ao usuário um número e retorne a tabuada de 1 ao 10 deste número.

#atribuímos o valor do número que queremos a tabuada e depois criamos um laço de repetição com a operacão e o print.
tab = float(input("digite o número que deseja saber a tabuada:"))
i = 0
for i in range(11):
    print(i*tab)
   
   # pedimos ao usuário para digitar o número que ele deseja a tabuada
   #  criamos um laço de repetição que vai multiplicar os números até 10
   # exibimos o resultado em tela para o usuário