#atribuimos nossa lista separada por vírgula, fatiamos por vírgula e contamos.
list = input("escreva sua lista separando-os por vírgula:")
def contador (list):
    return (len(list.split(",")))
print(contador(list))