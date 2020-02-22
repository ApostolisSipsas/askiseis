arxeio=input("δωσε αρχειο με πηνακα 3Χ3 :")
file=open(arxeio)
numbers=[[],[],[]]
count=0
for i in file:
    numbers[count]=i.split()
    count+=1
for i in range(3):
    for j in range(3):
        numbers[i][j]=int(numbers[i][j])
orizousa1=numbers[0][0]*((numbers[1][1]*numbers[2][2])-(numbers[1][2]*numbers[2][1]))
orizousa2=numbers[0][1]*((numbers[1][0]*numbers[2][2])-(numbers[1][2]*numbers[2][0]))
orizousa3=numbers[0][2]*((numbers[1][0]*numbers[2][1])-(numbers[1][1]*numbers[2][0]))
finor=orizousa1-orizousa2+orizousa3
print("η οριζουσα ειναι :",finor)
