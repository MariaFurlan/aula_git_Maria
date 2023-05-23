num1 = float(input('digite um número:'))
num2 = float(input('digite outro número:'))
calc =int(input('escolha a operação que deseja (1/2/3/4):'))
def adição(num1 ,num2):
    return num1 + num2
def subtração(num1 ,num2):
    return num1 - num2
def multiplicação(num1 ,num2):
    return num1 * num2
def divisão(num1 ,num2):
    return num1 / num2
if calc == 1:
    print(adição(num1,num2))
if calc == 2:
    print(subtração(num1,num2))
if calc == 3:
    print(multiplicação(num1,num2))
if calc == 4:
    print(divisão(num1,num2))

    