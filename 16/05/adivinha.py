from random import randint
def numero_aleatorio():
    aleatorio=randint(1,100)
    chute=0
    contador = 0
    while aleatorio != chute:
        contador += 1
        chute=int(input('digite um número de 1 a 100:'))
        if (aleatorio == chute):
            print('Muito Bem! Correto')
        if (aleatorio<chute):
            print('Tente um valor menor')    
        if (aleatorio>chute):
            print('Tente um valor maior')
    print("tentativas " + str(contador))

    

numero_aleatorio()

