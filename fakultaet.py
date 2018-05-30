#fakultaet.py

eingabe = int(input("Welche Zahl willst du wissen?"))

ergenis=0
num=1
for i in range (1,eingabe+1):
    num=num*i
print(eingabe,"! = ",num )