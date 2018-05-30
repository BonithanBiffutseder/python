#fibonatcci-numbers.py

eingabe = int(input("Wähle eine Zahl:"))

fz=0
letzteZahl=1
vorletzteZahl=1

for i in range(0, eingabe-1):  
    fz=letzteZahl +vorletzteZahl
    print(vorletzteZahl, letzteZahl,"=>", fz)
    vorletzteZahl= letzteZahl
    letzteZahl=fz