#wuerfeln.py

#100 mal würfeln simulieren
#anzahl der 1er, 2er usw. ausgeben

wuerfeln0 = 0
wuerfeln1 = 0
wuerfeln2 = 0
wuerfeln3 = 0
wuerfeln4 = 0
wuerfeln5 = 0
anzahl =100

for i in range (0,anzahl):
    wurf=0
    wurf=randint(1,6)
    if (wurf==1):
        wuerfeln0=wurf
    if(wurf==2):
        wuerfeln1=wurf
    if(wurf==3):
        wuerfeln2=wurf
    if(wurf==4):
        wuerfeln3=wurf
    if(wurf==5):
        wuerfeln4=wurf
    if(wurf==6):
        wuerfeln5=wurf
print("Es wirden [1]: "+ wuerfeln0)
print("          [2]: "+ wuerfeln1)
print("          [3]: "+ wuerfeln2)
print("          [4]: "+ wuerfeln3)
print("          [5]: "+ wuerfeln4)
print("          [6]: "+ wuerfeln5+" gewürfelt")