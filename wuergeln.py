#wuerfeln.py
from random import randint
#100 mal würfeln simulieren
#anzahl der 1er, 2er usw. ausgeben

wuerfeln0 = 0
wuerfeln1 = 0
wuerfeln2 = 0
wuerfeln3 = 0
wuerfeln4 = 0
wuerfeln5 = 0
anzahl = int(input("Wie oft soll gewürfelt werden?"))

for i in range (0,anzahl):
    wurf = randint(1,6)
    if (wurf==1):
        wuerfeln0+=1
    if(wurf==2):
        wuerfeln1+=1
    if(wurf==3):
        wuerfeln2+=1
    if(wurf==4):
        wuerfeln3+=1
    if(wurf==5):
        wuerfeln4+=1
    if(wurf==6):
        wuerfeln5+=1
print("Es werden [1]: ", wuerfeln0)
print("          [2]: ", wuerfeln1)
print("          [3]: ", wuerfeln2)
print("          [4]: ", wuerfeln3)
print("          [5]: ", wuerfeln4)
print("          [6]: ", wuerfeln5," gewürfelt")