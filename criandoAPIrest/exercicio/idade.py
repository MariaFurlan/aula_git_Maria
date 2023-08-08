import datetime
import math

anonasc = int(input("digite o ano do seu nascimento:"))
mesnasc = int(input("digite o mês do seu nascimento:"))
dianasc = int(input("digite o a dia seu nascimento:"))
birthday = datetime.date(anonasc, mesnasc, dianasc)
yn = datetime.date.today()

calculo = yn - birthday
print (math.floor(calculo.days/365))